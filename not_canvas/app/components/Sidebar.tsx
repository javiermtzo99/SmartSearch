// components/Sidebar.tsx

import React from 'react';
import Link from 'next/link';
import styles from './Sidebar.module.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser, faGauge, faBook, faCalendar, faEnvelope, faHistory, faQuestionCircle } from '@fortawesome/free-solid-svg-icons';


const Sidebar: React.FC = () => {
  return (
    <div className={styles.sidebar}>
      <div className={styles.logo}>
        <img src="/ubc_logo.png" alt="UBC Logo" className={styles.logoImage} />
      </div>
      <nav className={styles.nav}>
        <Link href="/" className={styles.link}>
          <FontAwesomeIcon icon={faUser} className={styles.icon} /> 
          Account
        </Link>
        <Link href="/" className={styles.link}>
          <FontAwesomeIcon icon={faGauge} className={styles.icon} /> Dashboard
        </Link>
        <Link href="/" className={`${styles.link} ${styles.activeLink}`}>
          <FontAwesomeIcon icon={faBook} className={styles.icon} /> Courses
        </Link>
        <Link href="/" className={styles.link}>
          <FontAwesomeIcon icon={faCalendar} className={styles.icon} /> Calendar
        </Link>
        <Link href="/" className={styles.link}>
          <FontAwesomeIcon icon={faEnvelope} className={styles.icon} /> Inbox
        </Link>
        <Link href="/" className={styles.link}>
          <FontAwesomeIcon icon={faHistory} className={styles.icon} /> History
        </Link>
        <Link href="/" className={styles.link}>
          <FontAwesomeIcon icon={faQuestionCircle} className={styles.icon} /> Help
        </Link>
      </nav>
    </div>
  );
};

export default Sidebar;
