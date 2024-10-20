// app/layout.tsx

"use client";

import React from 'react';
import Sidebar from './components/Sidebar'; // Import Sidebar component
import Header from './components/Header';
import './globals.css';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <Sidebar />
        <main style={{ marginLeft: '140px', marginTop: '20px'}}>
          <Header />
          {children}
        </main>
      </body>
    </html>
  );
}
