// components/VerticalNav.tsx

import React from 'react';
import styles from './VerticalNav.module.css';

const VerticalNav: React.FC = () => {
  return (
    <div className={styles.navContainer}>
      <div className={styles.version}>2024W1_V</div>

      <nav className={styles.nav}>
        {/* Static List of Links */}
        <div className={styles.navItem}>Home</div>
        <div className={styles.navItem}>Modules</div>
        <div className={`${styles.navItem} ${styles.activeNavItem}`}>
          Discussions
        </div>
        <div className={styles.navItem}>Announcements</div>
        <div className={styles.navItem}>Assignments</div>
        <div className={styles.navItem}>Grades</div>
        <div className={styles.navItem}>People</div>
        <div className={styles.navItem}>Pages</div>
        <div className={styles.navItem}>Syllabus</div>
        <div className={styles.navItem}>Quizzes</div>
        <div className={styles.navItem}>Chat</div>
        <div className={styles.navItem}>Threadz</div>
      </nav>
    </div>
  );
};

export default VerticalNav;
