// src/components/SenderItem.js
import React from 'react';
import { unsubscribeSender } from '../api/unsubscribe';

function SenderItem({ sender, accessToken, onUnsubscribed }) {
  const handleUnsubscribe = async () => {
    try {
      await unsubscribeSender({
        unsubscribe_url: sender.unsubscribe_url,
        unsubscribe_mailto: sender.unsubscribe_mailto,
        access_token: accessToken
      });

      alert(`Unsubscribed from ${sender.email}`);
      onUnsubscribed(sender.email);  // optional callback to update UI
    } catch (err) {
      console.error(err);
      alert(`Failed to unsubscribe: ${err.message}`);
    }
  };

  return (
    <div className="sender-item">
      <div>
        <strong>{sender.email}</strong> ({sender.count} emails)
      </div>
      <button onClick={handleUnsubscribe}>Unsubscribe</button>
    </div>
  );
}

export default SenderItem;
