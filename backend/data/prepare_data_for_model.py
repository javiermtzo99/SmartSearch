import pandas as pd
import re

# Function to extract text inside <p> and links
def extract_message_and_links(html_text):
    # Extract content inside <p> tags
    message_content = re.findall(r'<p>(.*?)</p>', html_text, re.DOTALL)
    message_text = " ".join(message_content)  # Join in case of multiple <p> tags
    
    # Extract links after href=
    links = re.findall(r'href="(.*?)"', html_text)
    links_text = ", ".join(links)  # Join multiple links

    # Combine message and links
    cleaned_message = f"{message_text}. Links: {links_text}"
    return cleaned_message

def get_discussions_data_ready_for_model(discussions_df:pd.DataFrame):
    # Apply the extraction function to the message column
    discussions_df['cleaned_message'] = discussions_df['message'].apply(extract_message_and_links)

    # Create the new dataframe
    discussions_ready_for_model = pd.DataFrame({
        'discussion_id': discussions_df['id'],
        'discussion_text': "Title: " + discussions_df['title'] + ", Message: " + discussions_df['cleaned_message']
    })
    return discussions_ready_for_model