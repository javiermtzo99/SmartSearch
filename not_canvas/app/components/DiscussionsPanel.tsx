// components/DiscussionsPanel.tsx
"use client";
import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import styles from './DiscussionsPanel.module.css';

interface Discussion {
  id: number;
  discussion_title: string;
  date: string;
}

const DiscussionsPanel: React.FC = () => {
  const [discussions, setDiscussions] = useState<Discussion[]>([]);

  // Fetch discussions data from the API
  useEffect(() => {
    fetch('http://localhost:5001/discussions')
      .then((response) => response.json())
      .then((data) => setDiscussions(data));
  }, []);

  return (
    <div className={styles.panel}>
      <h2 className={styles.title}>Discussions</h2>
      {discussions.map((discussion) => (
        <Link
          key={discussion.id}
          href={`/discussions/${discussion.id}`}
          className={styles.discussionItem}
        >
          <div className={styles.discussionTitle}>{discussion.discussion_title}</div>
          <div className={styles.discussionDate}>{discussion.date}</div>
        </Link>
      ))}
    </div>
  );
};

export default DiscussionsPanel;

