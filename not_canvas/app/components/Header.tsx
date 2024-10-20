// components/Header.tsx

import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBars } from '@fortawesome/free-solid-svg-icons';
import styles from './Header.module.css';

const Header: React.FC = () => {
  return (
    <div>
        <div className={styles.headerContainer}>
            <div className={styles.menuIcon}>
                <FontAwesomeIcon icon={faBars} />
            </div>

            <div className={styles.courseTitle}>
                <a href="/" className={styles.link}>hack-la-24</a>
            </div>

            <div className={styles.pageTitle}>
                <span>&gt;</span>
            </div>

            <div className={styles.pageTitle}>
                <span>Discussions</span>
            </div>
        </div>
    </div>
  );
};

export default Header;
