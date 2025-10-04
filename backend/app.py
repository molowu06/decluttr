from flask import Flask, jsonify
from gmail_api import get_parsed_emails
from aggregate_senders import aggregate_senders
from unsubscribe import unsubscribe_bp  # import Blueprint

app = Flask(__name__)
app.register_blueprint(unsubscribe_bp)

# Access token placeholder (to be replaced with real token handling)
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN_HERE'

@app.route('/api/emails')
def get_emails():
    try:
        query = 'after:2023/09/01'
        emails = get_parsed_emails(ACCESS_TOKEN, query)
        dashboard_data = aggregate_senders(emails, min_count=5)
        return jsonify(dashboard_data)  # send dashboard data
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

