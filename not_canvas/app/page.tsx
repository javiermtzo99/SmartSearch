// app/page.tsx

import React from 'react';
import VerticalNav from './components/VerticalNav';
import Toolbar from './components/Toolbar';
import DiscussionsPanel from './components/DiscussionsPanel';
import SearchBar from './components/SearchBar'

const HomePage: React.FC = () => {
  return (
    <div style={{ display: 'flex' }}>
      <VerticalNav />
      <div style={{ marginLeft: '60px', padding: '20px' }}>
        <Toolbar />
        <SearchBar />
        <DiscussionsPanel />
      </div>
    </div>
  );
};

export default HomePage;
