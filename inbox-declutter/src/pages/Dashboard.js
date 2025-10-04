// src/pages/Dashboard.js
import React, { useEffect, useState } from 'react';
import SenderList from '../components/SenderList';

function Dashboard({ accessToken }) {
  const [senders, setSenders] = useState([]);

  useEffect(() => {
    async function fetchEmails() {
      const res = await fetch('/api/emails');
      const data = await res.json();
      setSenders(data);  // assuming backend returns array of senders
    }

    fetchEmails();
  }, []);

  return (
    <div>
      <h2>Top Senders This Month</h2>
      <SenderList
        senders={senders}
        accessToken={accessToken}
        onUnsubscribed={(email) =>
          setSenders(prev => prev.filter(s => s.email !== email))
        }
      />
    </div>
  );
}

export default Dashboard;

