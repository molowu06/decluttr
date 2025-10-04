import base64
from email.utils import parseaddr
from urllib.parse import unquote

def parse_email_message(message):
    headers = {h['name']: h['value'] for h in message['payload']['headers']}

    # Parse sender email (name + email)
    sender_name, sender_email = parseaddr(headers.get('From', ''))

    subject = headers.get('Subject', '')
    date = headers.get('Date', '')

    # Extract unsubscribe info (may have multiple URLs/emails)
    unsubscribe_raw = headers.get('List-Unsubscribe', '')
    unsubscribe_links = []

    # Parse List-Unsubscribe header, split by comma, strip <> and whitespace
    if unsubscribe_raw:
        parts = [part.strip() for part in unsubscribe_raw.split(',')]
        for part in parts:
            # Remove <> if present
            link = part.strip('<>')
            # Some links are mailto: or https://
            unsubscribe_links.append(link)

    # Decode body (optional - fetch plain text part)
    body = ''
    if 'parts' in message['payload']:
        for part in message['payload']['parts']:
            if part['mimeType'] == 'text/plain':
                body_data = part['body'].get('data')
                if body_data:
                    body = base64.urlsafe_b64decode(body_data.encode('UTF-8')).decode('UTF-8')
                    break

    return {
        'sender_name': sender_name,
        'sender_email': sender_email,
        'subject': subject,
        'date': date,
        'unsubscribe_links': unsubscribe_links,
        'body_snippet': body[:200]  # optional snippet preview
    }
