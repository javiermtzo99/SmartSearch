import os
from dotenv import load_dotenv
from canvasapi import Canvas
import pandas as pd

# Load environment variables from .env file
load_dotenv()

def get_canvas_data():
    """
    Retrieve discussions and replies from Canvas and return them as dataframes.
    """
    # Get environment variables
    API_URL = os.getenv('CANVAS_API_URL')
    API_KEY = os.getenv('CANVAS_API_KEY')
    COURSE_ID = os.getenv('CANVAS_COURSE_ID')

    # Ensure variables are set
    if not all([API_URL, API_KEY, COURSE_ID]):
        raise ValueError("API_URL, API_KEY, and COURSE_ID must be set in environment variables")

    # Initialize Canvas API
    canvas = Canvas(API_URL, API_KEY)
    course = canvas.get_course(int(COURSE_ID))

    # Lists to store discussion and reply data
    discussion_data = []
    reply_data = []

    # Get all discussions for the course
    discussions = course.get_discussion_topics()
    for discussion in discussions:
        discussion_data.append({
            'id': discussion.id,
            'title': discussion.title,
            'message': discussion.message,
            'posted_at': discussion.posted_at,
            'user_name': discussion.user_name,
            'discussion_type': discussion.discussion_type,
            'published': discussion.published,
            'locked': discussion.locked,
            'locked_for_user': discussion.locked_for_user,
            'delayed_post_at': discussion.delayed_post_at,
            'require_initial_post': discussion.require_initial_post,
            'subscribed': discussion.subscribed,
            'read_state': discussion.read_state,
            'assignment_id': discussion.assignment_id,
            'group_category_id': discussion.group_category_id,
            'root_topic_id': discussion.root_topic_id
        })

        # Get all entries (replies) for the current discussion
        entries = discussion.get_topic_entries()
        for entry in entries:
            reply_data.append({
                'discussion_id': discussion.id,
                'entry_id': entry.id,
                'user_id': entry.user_id,
                'user_name': entry.user_name,
                'created_at': entry.created_at,
                'updated_at': entry.updated_at,
                'message': entry.message,
                'read_state': entry.read_state,
                'parent_entry_id': entry.parent_id
            })

    # Convert to DataFrames
    discussions_df = pd.DataFrame(discussion_data)
    replies_df = pd.DataFrame(reply_data)

    return discussions_df, replies_df
