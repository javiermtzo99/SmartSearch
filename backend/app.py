from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from flask_cors import CORS 
from data.canvas_retrieval import get_canvas_data
from model.index_model import get_index_and_model
from data.prepare_data_for_model import get_discussions_data_ready_for_model, extract_message_and_links
from data.demo_data import return_demo_data

# Initialize Flask app
app = Flask(__name__)

CORS(app)

# Canvas dataset
discussions_df, replies_df = get_canvas_data()

# Test dataset
# discussions_df, replies_df = return_demo_data()

df = get_discussions_data_ready_for_model(discussions_df)
model, index = get_index_and_model(df)

@app.route('/discussions', methods=['GET'])
def get_discussions():
    # Transform discussions_df to the required JSON format
    discussions_json = [
        {
            "id": int(row['id']),
            "discussion_title": row['title'],
            "date": f"Last post at {pd.to_datetime(row['posted_at']).strftime('%b %d, %I:%M %p')}"
        }
        for _, row in discussions_df.iterrows()
    ]

    return jsonify(discussions_json)

@app.route('/discussions/<int:id>', methods=['GET'])
def get_discussion_by_id(id):
    # Filter the dataframe for the specific discussion ID
    discussion_row = discussions_df[discussions_df['id'] == id]

    if discussion_row.empty:
        return jsonify({'error': 'Discussion not found'}), 404

    # Transform the row into JSON format
    discussion = {
        "id": int(discussion_row.iloc[0]['id']),
        "discussion_title": discussion_row.iloc[0]['title'],
        "date": f"Last post at {pd.to_datetime(discussion_row.iloc[0]['posted_at']).strftime('%b %d, %I:%M %p')}",
        "discussion_description": f"This is a detailed description of the discussion titled '{discussion_row.iloc[0]['title']}'."
    }

    return jsonify(discussion)

@app.route('/discussions/<int:id>/replies', methods=['GET'])
def get_replies_by_discussion_id(id):
    # Filter the dataframe for the specific discussion ID
    replies = replies_df[replies_df['discussion_id'] == id]

    if replies.empty:
        return jsonify({'error': 'No replies found for this discussion'}), 404

    # Sort by 'entry_id' in ascending order
    replies = replies.sort_values(by='entry_id')

    # Transform the rows into JSON format matching the specified interface
    replies_json = [
        {
            "id": int(row['entry_id']),  # Use 'entry_id' as the reply ID
            "author": row['user_name'],
            "text": row['message'],
            "date": pd.to_datetime(row['created_at']).strftime('%b %d, %I:%M %p')
        }
        for _, row in replies.iterrows()
    ]

    return jsonify(replies_json)

@app.route('/search', methods=['POST'])
def search():
    # Check if the content type is 'application/json'
    if request.content_type != 'application/json':
        return jsonify({'error': 'Content-Type must be application/json'}), 415

    # Read JSON data from the request
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON data'}), 400

    query_text = data.get('query', '')
    threshold = 1.5
    k = 5

    # Generate embedding for the query
    query_embedding = model.encode([query_text])

    # Perform the search for the nearest neighbors
    distances, indices = index.search(np.array(query_embedding), k)

    # Filter results based on the threshold
    results = [
        {
            'discussion_id': int(df.iloc[idx]['discussion_id']),
            'discussion_text': df.iloc[idx]['discussion_text'],
            'distance': float(dist)
        }
        for idx, dist in zip(indices[0], distances[0]) if dist <= threshold
    ]

    # Return the results as JSON
    return jsonify({'query': query_text, 'results': results})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

# Initialize Flask app
app = Flask(__name__)
