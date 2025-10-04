# backend/gmail_api.py

import requests
from email_parser import parse_email_message  # Import your parser function

def list_message_ids(access_token, query, page_token=None):
    url = 'https://gmail.googleapis.com/gmail/v1/users/me/messages'
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {'q': query}
    if page_token:
        params['pageToken'] = page_token

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def get_message_details(access_token, message_id):
    url = f'https://gmail.googleapis.com/gmail/v1/users/me/messages/{message_id}'
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {'format': 'full'}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def get_parsed_emails(access_token, query=''):
    parsed_emails = []
    page_token = None

    while True:
        messages_response = list_message_ids(access_token, query, page_token)
        messages = messages_response.get('messages', [])

        for msg in messages:
            msg_detail = get_message_details(access_token, msg['id'])
            parsed_email = parse_email_message(msg_detail)
            parsed_emails.append(parsed_email)

        page_token = messages_response.get('nextPageToken')
        if not page_token:
            break

    return parsed_emails
