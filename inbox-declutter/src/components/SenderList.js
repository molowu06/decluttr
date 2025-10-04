// src/components/SenderList.js
import React from 'react';
import SenderItem from './SenderItem';

function SenderList({ senders, accessToken, onUnsubscribed }) {
  return (
    <div className="sender-list">
      {senders.map(sender => (
        <SenderItem
          key={sender.email}
          sender={sender}
          accessToken={accessToken}
          onUnsubscribed={onUnsubscribed}
        />
      ))}
    </div>
  );
}

export default SenderList;
