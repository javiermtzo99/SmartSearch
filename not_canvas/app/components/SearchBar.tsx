"use client";
import React, { useState } from 'react';
import Link from 'next/link';
import styles from './SearchBar.module.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch } from '@fortawesome/free-solid-svg-icons';

interface SearchResult {
  discussion_id: number;
  discussion_text: string;
  distance: number;
}

const SearchBar: React.FC = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<SearchResult[]>([]);
  const [showPopup, setShowPopup] = useState(false);

  const handleSearch = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const input = event.target.value;
    setQuery(input);

    if (input.length > 0) {
      try {
        const response = await fetch('http://localhost:5001/search', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ query: input }),
        });

        if (response.ok) {
          const data = await response.json();
          setResults(data.results);
          setShowPopup(true);
        } else {
          console.error('Search failed:', response.status);
        }
      } catch (error) {
        console.error('Error fetching search results:', error);
      }
    } else {
      setShowPopup(false);
    }
  };

  return (
    <div className={styles.searchBarModule}>
      <div className={styles.searchBar}>
        <FontAwesomeIcon icon={faSearch} className={styles.searchIcon} />
        <input
          type="text"
          placeholder="SmartSearch"
          value={query}
          onChange={handleSearch}
        />
      </div>

      {/* Popup for displaying search results */}
            {results.map((result) => {
            // Extract the title part from discussion_text
            const discussionTitle = result.discussion_text
              .split('Title: ')[1]
              .split(', Message:')[0];

            return (
              <div key={result.discussion_id} className={styles.resultItem}>
                <Link
                  href={`/discussions/${result.discussion_id}`}
                  onClick={() => setShowPopup(false)} // Close popup on click
                >
                  {discussionTitle}
                </Link>
              </div>
            );
          })}

      {showPopup && results.length === 0 && (
        <div className={styles.noResults}>No results found</div>
      )}
    </div>
  );
};

export default SearchBar;
