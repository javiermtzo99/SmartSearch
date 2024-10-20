// components/Toolbar.tsx

import React from 'react';
import styles from './Toolbar.module.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch, faCog, faPlus } from '@fortawesome/free-solid-svg-icons';

const Toolbar: React.FC = () => {
  return (
    <div className={styles.toolbar}>
      <div className={styles.dropdown}>
        <select>
          <option value="all">All</option>
          <option value="option1">Unread</option>
        </select>
      </div>

      <button className={styles.addButton}>
        <FontAwesomeIcon icon={faPlus} className={styles.plusIcon} /> Discussion
      </button>

      <div className={styles.settings}>
        <FontAwesomeIcon icon={faCog} className={styles.cogIcon} />
      </div>
    </div>
  );
};

export default Toolbar;
