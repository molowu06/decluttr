// src/api/unsubscribe.js
export async function unsubscribeSender({ unsubscribe_url, unsubscribe_mailto, access_token }) {
  const res = await fetch('/api/unsubscribe', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ unsubscribe_url, unsubscribe_mailto, access_token })
  });

  const result = await res.json();

  if (!res.ok) {
    throw new Error(result.error || 'Failed to unsubscribe');
  }

  return result;
}
