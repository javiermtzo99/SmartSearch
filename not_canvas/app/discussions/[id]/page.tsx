"use client";

import { useParams } from 'next/navigation';
import { useEffect, useState } from 'react';
import styles from './DiscussionDetails.module.css';
import VerticalNav from '../../components/VerticalNav';
import Toolbar from '../../components/Toolbar';

interface DiscussionDetails {
  discussion_title: string;
  discussion_description: string;
  date: string;
}

interface Reply {
  id: number;
  author: string;
  text: string;
  date: string;
}

const DiscussionDetails: React.FC = () => {
  const params = useParams();
  const id = params.id ? String(params.id) : ''; // Convert to string
  const [discussion, setDiscussion] = useState<DiscussionDetails | null>(null);
  const [replies, setReplies] = useState<Reply[]>([]);

  useEffect(() => {
    if (id) {
      // Fetch discussion details from the backend
      fetch(`http://localhost:5001/discussions/${id}`)
        .then((response) => {
          if (!response.ok) {
            throw new Error('Failed to fetch discussion');
          }
          return response.json();
        })
        .then((data) => setDiscussion(data))
        .catch((error) => console.error('Error fetching discussion:', error));

      // Fetch replies for the specific discussion ID from the backend
      fetch(`http://localhost:5001/discussions/${id}/replies`)
        .then((response) => {
          if (!response.ok) {
            throw new Error('Failed to fetch replies');
          }
          return response.json();
        })
        .then((data) => setReplies(data))
        .catch((error) => console.error('Error fetching replies:', error));
    }
  }, [id]);

  if (!discussion) {
    return <div>Loading...</div>;
  }

  return (
    <div style={{ display: 'flex' }}>
      <VerticalNav />
      <div style={{ marginLeft: '60px', padding: '20px' }}>
        <Toolbar />
        <div className={styles.detailsContainer}>
          <div className={styles.header}>
            <h1 className={styles.title}>{discussion.discussion_title}</h1>
            <p className={styles.date}>{discussion.date}</p>
            <p className={styles.description}>{discussion.discussion_description}</p>
            <button className={styles.replyButton}>Reply</button>
          </div>

          {/* Display replies */}
          <div className={styles.replies}>
            {replies.map((reply) => (
              <div key={reply.id} className={styles.replyItem}>
                <div className={styles.replyAuthor}>{reply.author}</div>
                <div className={styles.replyDate}>{reply.date}</div>
                <div className={styles.replyText}>{reply.text}</div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default DiscussionDetails;
