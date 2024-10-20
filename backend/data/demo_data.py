import pandas as pd
from datetime import datetime, timedelta

# Helper function to generate timestamps
def generate_timestamp(days_ago):
    return (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%dT%H:%M:%SZ')

# Create discussion data
discussion_data = pd.DataFrame([
    # Terminology, Baselines, Decision Trees
    {
        'id': 1, 'title': 'Terminology in Supervised Learning', 'message': 'Let’s discuss common terminology.',
        'posted_at': generate_timestamp(7), 'user_name': 'Alice Johnson', 'discussion_type': 'topic',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': False, 'subscribed': True, 'read_state': 'read', 'assignment_id': None,
        'group_category_id': None, 'root_topic_id': 1
    },
    {
        'id': 2, 'title': 'Decision Trees: Basics', 'message': 'Understanding Decision Trees.',
        'posted_at': generate_timestamp(5), 'user_name': 'Bob Smith', 'discussion_type': 'topic',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': False, 'subscribed': True, 'read_state': 'unread', 'assignment_id': None,
        'group_category_id': None, 'root_topic_id': 2
    },
    # Machine Learning Fundamentals
    {
        'id': 3, 'title': 'ML Fundamentals', 'message': 'Core concepts in ML.',
        'posted_at': generate_timestamp(6), 'user_name': 'Charlie Brown', 'discussion_type': 'topic',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': True, 'subscribed': True, 'read_state': 'read', 'assignment_id': None,
        'group_category_id': None, 'root_topic_id': 3
    },
    {
        'id': 4, 'title': 'Supervised Learning Basics', 'message': 'Let’s explore supervised learning.',
        'posted_at': generate_timestamp(4), 'user_name': 'Diana Lee', 'discussion_type': 'topic',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': True, 'subscribed': False, 'read_state': 'unread', 'assignment_id': None,
        'group_category_id': None, 'root_topic_id': 4
    },
    # K-Nearest Neighbours and SVM RBFs
    {
        'id': 5, 'title': 'KNN Explained', 'message': 'How does K-Nearest Neighbours work?',
        'posted_at': generate_timestamp(3), 'user_name': 'Ethan Clark', 'discussion_type': 'topic',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': False, 'subscribed': True, 'read_state': 'read', 'assignment_id': None,
        'group_category_id': None, 'root_topic_id': 5
    },
    {
        'id': 6, 'title': 'SVM RBFs', 'message': 'Let’s discuss SVM with RBF kernels.',
        'posted_at': generate_timestamp(2), 'user_name': 'Fiona Green', 'discussion_type': 'topic',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': False, 'subscribed': False, 'read_state': 'unread', 'assignment_id': None,
        'group_category_id': None, 'root_topic_id': 6
    },
    # Preprocessing, sklearn Pipeline, sklearn ColumnTransformer
    {
        'id': 7, 'title': 'Preprocessing in ML', 'message': 'How to preprocess data in ML?',
        'posted_at': generate_timestamp(1), 'user_name': 'George Harris', 'discussion_type': 'topic',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': True, 'subscribed': True, 'read_state': 'read', 'assignment_id': None,
        'group_category_id': None, 'root_topic_id': 7
    },
    {
        'id': 8, 'title': 'Sklearn Pipelines', 'message': 'Implementing pipelines in sklearn.',
        'posted_at': generate_timestamp(0), 'user_name': 'Helen Martin', 'discussion_type': 'topic',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': False, 'subscribed': True, 'read_state': 'unread', 'assignment_id': None,
        'group_category_id': None, 'root_topic_id': 8
    },
    {
        'id': 9, 'title': 'Assignment 1: Decision Trees', 'message': 'Questions about Assignment 1.',
        'posted_at': generate_timestamp(10), 'user_name': 'Olivia Brown', 'discussion_type': 'assignment',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': True, 'subscribed': True, 'read_state': 'read', 'assignment_id': 1,
        'group_category_id': None, 'root_topic_id': 9
    },
    {
        'id': 10, 'title': 'Quiz 1: ML Basics', 'message': 'Discussion about Quiz 1 topics.',
        'posted_at': generate_timestamp(9), 'user_name': 'Paul Green', 'discussion_type': 'quiz',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': False, 'subscribed': True, 'read_state': 'unread', 'assignment_id': None,
        'group_category_id': None, 'root_topic_id': 10
    },
    {
        'id': 11, 'title': 'Lab 2: KNN Implementation', 'message': 'Issues with Lab 2 implementation.',
        'posted_at': generate_timestamp(8), 'user_name': 'Quinn Harris', 'discussion_type': 'lab',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': True, 'subscribed': False, 'read_state': 'read', 'assignment_id': 2,
        'group_category_id': None, 'root_topic_id': 11
    },
    {
        'id': 12, 'title': 'Assignment 2: SVMs', 'message': 'Let’s discuss Assignment 2 questions.',
        'posted_at': generate_timestamp(7), 'user_name': 'Rachel Clark', 'discussion_type': 'assignment',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': True, 'subscribed': True, 'read_state': 'unread', 'assignment_id': 2,
        'group_category_id': None, 'root_topic_id': 12
    },
    {
        'id': 13, 'title': 'Quiz 2: Preprocessing', 'message': 'Questions about Quiz 2 content.',
        'posted_at': generate_timestamp(6), 'user_name': 'Sam Black', 'discussion_type': 'quiz',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': False, 'subscribed': True, 'read_state': 'read', 'assignment_id': None,
        'group_category_id': None, 'root_topic_id': 13
    },
    {
        'id': 14, 'title': 'Lab 3: Sklearn Pipelines', 'message': 'Help with Lab 3 pipelines.',
        'posted_at': generate_timestamp(5), 'user_name': 'Tina Turner', 'discussion_type': 'lab',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': True, 'subscribed': True, 'read_state': 'unread', 'assignment_id': 3,
        'group_category_id': None, 'root_topic_id': 14
    },
    {
        'id': 15, 'title': 'Assignment 3: Sklearn Transformers', 'message': 'Discussion about transformers.',
        'posted_at': generate_timestamp(4), 'user_name': 'Uma White', 'discussion_type': 'assignment',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': False, 'subscribed': True, 'read_state': 'read', 'assignment_id': 3,
        'group_category_id': None, 'root_topic_id': 15
    },
    {
        'id': 16, 'title': 'Quiz 3: Supervised Learning Overview', 'message': 'Clarifications about Quiz 3.',
        'posted_at': generate_timestamp(3), 'user_name': 'Victor Hugo', 'discussion_type': 'quiz',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': True, 'subscribed': False, 'read_state': 'unread', 'assignment_id': None,
        'group_category_id': None, 'root_topic_id': 16
    },
    {
        'id': 17, 'title': 'Lab 4: Advanced Decision Trees', 'message': 'Lab 4 advanced concepts.',
        'posted_at': generate_timestamp(2), 'user_name': 'Wendy Adams', 'discussion_type': 'lab',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': True, 'subscribed': True, 'read_state': 'unread', 'assignment_id': 4,
        'group_category_id': None, 'root_topic_id': 17
    },
    {
        'id': 18, 'title': 'Assignment 4: Preprocessing Data', 'message': 'Assignment 4 discussions.',
        'posted_at': generate_timestamp(1), 'user_name': 'Xander Fox', 'discussion_type': 'assignment',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': True, 'subscribed': True, 'read_state': 'read', 'assignment_id': 4,
        'group_category_id': None, 'root_topic_id': 18
    },
    {
        'id': 19, 'title': 'Quiz 4: Column Transformers', 'message': 'Discussion about Quiz 4 content.',
        'posted_at': generate_timestamp(1), 'user_name': 'Yara Green', 'discussion_type': 'quiz',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': False, 'subscribed': True, 'read_state': 'unread', 'assignment_id': None,
        'group_category_id': None, 'root_topic_id': 19
    },
    {
        'id': 20, 'title': 'Lab 5: Feature Scaling', 'message': 'Lab 5 scaling techniques.',
        'posted_at': generate_timestamp(0), 'user_name': 'Zara White', 'discussion_type': 'lab',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': True, 'subscribed': True, 'read_state': 'unread', 'assignment_id': 5,
        'group_category_id': None, 'root_topic_id': 20
    },
    {
        'id': 21, 'title': 'Assignment 5: Evaluating Models', 'message': 'Discussion on evaluation techniques.',
        'posted_at': generate_timestamp(2), 'user_name': 'Adam Bell', 'discussion_type': 'assignment',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': True, 'subscribed': True, 'read_state': 'read', 'assignment_id': 5,
        'group_category_id': None, 'root_topic_id': 21
    },
    {
        'id': 22, 'title': 'Quiz 5: Hyperparameter Tuning', 'message': 'Discussion on tuning hyperparameters.',
        'posted_at': generate_timestamp(3), 'user_name': 'Bella Clark', 'discussion_type': 'quiz',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': False, 'subscribed': True, 'read_state': 'read', 'assignment_id': None,
        'group_category_id': None, 'root_topic_id': 22
    },
    {
        'id': 23, 'title': 'Lab 6: Cross-Validation', 'message': 'Issues with cross-validation techniques.',
        'posted_at': generate_timestamp(4), 'user_name': 'Carl Davis', 'discussion_type': 'lab',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': True, 'subscribed': True, 'read_state': 'unread', 'assignment_id': 6,
        'group_category_id': None, 'root_topic_id': 23
    },
    {
        'id': 24, 'title': 'Assignment 6: Model Deployment', 'message': 'Discussion on deploying models.',
        'posted_at': generate_timestamp(5), 'user_name': 'Dana Evans', 'discussion_type': 'assignment',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': True, 'subscribed': True, 'read_state': 'unread', 'assignment_id': 6,
        'group_category_id': None, 'root_topic_id': 24
    },
    {
        'id': 25, 'title': 'Quiz 6: Pipelines in Practice', 'message': 'Quiz 6 discussion.',
        'posted_at': generate_timestamp(6), 'user_name': 'Eva White', 'discussion_type': 'quiz',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': False, 'subscribed': True, 'read_state': 'unread', 'assignment_id': None,
        'group_category_id': None, 'root_topic_id': 25
    },
    {
        'id': 26, 'title': 'Lab 7: Advanced Pipelines', 'message': 'Discussion on advanced pipeline features.',
        'posted_at': generate_timestamp(7), 'user_name': 'Frank Gordon', 'discussion_type': 'lab',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': True, 'subscribed': True, 'read_state': 'read', 'assignment_id': 7,
        'group_category_id': None, 'root_topic_id': 26
    },
    {
        'id': 27, 'title': 'Assignment 7: Ensemble Learning', 'message': 'Discussion about ensemble methods.',
        'posted_at': generate_timestamp(8), 'user_name': 'Grace Lee', 'discussion_type': 'assignment',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': False, 'subscribed': True, 'read_state': 'unread', 'assignment_id': 7,
        'group_category_id': None, 'root_topic_id': 27
    },
    {
        'id': 28, 'title': 'Quiz 7: Boosting & Bagging', 'message': 'Discussion about boosting and bagging.',
        'posted_at': generate_timestamp(9), 'user_name': 'Henry Adams', 'discussion_type': 'quiz',
        'published': True, 'locked': False, 'locked_for_user': False, 'delayed_post_at': None,
        'require_initial_post': False, 'subscribed': True, 'read_state': 'unread', 'assignment_id': None,
        'group_category_id': None, 'root_topic_id': 28
    }
])

# Create reply data
reply_data = pd.DataFrame([
    # Replies for discussion 1
    {'discussion_id': 1, 'entry_id': 1001, 'user_id': 201, 'user_name': 'Ivy Wilson',
     'created_at': generate_timestamp(6), 'updated_at': generate_timestamp(5),
     'message': 'Can you explain the difference between classification and regression?',
     'read_state': 'read', 'parent_entry_id': None},
    {'discussion_id': 1, 'entry_id': 1002, 'user_id': 202, 'user_name': 'Jack Adams',
     'created_at': generate_timestamp(5), 'updated_at': generate_timestamp(4),
     'message': 'Classification predicts categories, while regression predicts continuous values.',
     'read_state': 'read', 'parent_entry_id': 1001},
    # Replies for discussion 2
    {'discussion_id': 2, 'entry_id': 1003, 'user_id': 203, 'user_name': 'Kathy Young',
     'created_at': generate_timestamp(4), 'updated_at': generate_timestamp(3),
     'message': 'What is information gain in Decision Trees?',
     'read_state': 'unread', 'parent_entry_id': None},
    {'discussion_id': 2, 'entry_id': 1004, 'user_id': 204, 'user_name': 'Larry King',
     'created_at': generate_timestamp(3), 'updated_at': generate_timestamp(2),
     'message': 'It measures the reduction in entropy after splitting.',
     'read_state': 'unread', 'parent_entry_id': 1003},
    # Additional replies for other discussions
    {'discussion_id': 3, 'entry_id': 1005, 'user_id': 205, 'user_name': 'Mary Johnson',
     'created_at': generate_timestamp(2), 'updated_at': generate_timestamp(1),
     'message': 'How does supervised learning differ from unsupervised learning?',
     'read_state': 'read', 'parent_entry_id': None},
    {'discussion_id': 4, 'entry_id': 1006, 'user_id': 206, 'user_name': 'Nathaniel Reed',
     'created_at': generate_timestamp(1), 'updated_at': generate_timestamp(0),
     'message': 'Supervised learning uses labeled data, while unsupervised doesn’t.',
     'read_state': 'read', 'parent_entry_id': 1005},
     {'discussion_id': 9, 'entry_id': 2001, 'user_id': 301, 'user_name': 'George Adams',
     'created_at': generate_timestamp(9), 'updated_at': generate_timestamp(8),
     'message': 'I have a question about Gini impurity in Assignment 1.', 'read_state': 'read', 'parent_entry_id': None},
    {'discussion_id': 10, 'entry_id': 2002, 'user_id': 302, 'user_name': 'Holly Brown',
     'created_at': generate_timestamp(8), 'updated_at': generate_timestamp(7),
     'message': 'How to answer the last question of Quiz 1?', 'read_state': 'unread', 'parent_entry_id': None},
    {'discussion_id': 11, 'entry_id': 2003, 'user_id': 303, 'user_name': 'Ian Clark',
     'created_at': generate_timestamp(7), 'updated_at': generate_timestamp(6),
     'message': 'Having trouble with KNN implementation in Lab 2.', 'read_state': 'read', 'parent_entry_id': None},
    {'discussion_id': 12, 'entry_id': 2004, 'user_id': 304, 'user_name': 'Jane Doe',
     'created_at': generate_timestamp(6), 'updated_at': generate_timestamp(5),
     'message': 'What are the steps to complete Assignment 2?', 'read_state': 'unread', 'parent_entry_id': None},
    {'discussion_id': 13, 'entry_id': 2005, 'user_id': 305, 'user_name': 'Kevin Evans',
     'created_at': generate_timestamp(5), 'updated_at': generate_timestamp(4),
     'message': 'Can you explain question 3 of Quiz 2?', 'read_state': 'read', 'parent_entry_id': None},
    {'discussion_id': 14, 'entry_id': 2006, 'user_id': 306, 'user_name': 'Linda Green',
     'created_at': generate_timestamp(4), 'updated_at': generate_timestamp(3),
     'message': 'Issues with Sklearn pipeline creation in Lab 3.', 'read_state': 'read', 'parent_entry_id': None},
    {'discussion_id': 15, 'entry_id': 2007, 'user_id': 307, 'user_name': 'Mike Harris',
     'created_at': generate_timestamp(3), 'updated_at': generate_timestamp(2),
     'message': 'How to implement ColumnTransformer in Assignment 3?', 'read_state': 'read', 'parent_entry_id': None},
    {'discussion_id': 16, 'entry_id': 2008, 'user_id': 308, 'user_name': 'Nina Johnson',
     'created_at': generate_timestamp(2), 'updated_at': generate_timestamp(1),
     'message': 'Any hints for the last question of Quiz 3?', 'read_state': 'unread', 'parent_entry_id': None},
    {'discussion_id': 17, 'entry_id': 2009, 'user_id': 309, 'user_name': 'Oliver King',
     'created_at': generate_timestamp(1), 'updated_at': generate_timestamp(0),
     'message': 'Stuck with advanced Decision Trees in Lab 4.', 'read_state': 'read', 'parent_entry_id': None}
])

def return_demo_data():
    return discussion_data, reply_data
