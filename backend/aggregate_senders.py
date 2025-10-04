from collections import defaultdict

def aggregate_senders(emails, min_count=5):
    sender_counts = defaultdict(int)
    sender_data = {}

    for email in emails:
        sender = email['sender_email']
        sender_counts[sender] += 1
        if sender not in sender_data:
            sender_data[sender] = {
                'sender_name': email['sender_name'],
                'unsubscribe_links': email['unsubscribe_links'],
                'example_subjects': [email['subject']],
            }
        else:
            # Add up to 3 example subjects
            if len(sender_data[sender]['example_subjects']) < 3:
                sender_data[sender]['example_subjects'].append(email['subject'])

    # Filter senders with at least min_count emails
    result = []
    for sender, count in sender_counts.items():
        if count >= min_count:
            info = sender_data[sender]
            result.append({
                'sender_email': sender,
                'sender_name': info['sender_name'],
                'email_count': count,
                'unsubscribe_links': info['unsubscribe_links'],
                'example_subjects': info['example_subjects']
            })

    return result
