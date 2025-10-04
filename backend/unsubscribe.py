from flask import Blueprint, request, jsonify
import requests
from gmail_api import send_unsubscribe_email

unsubscribe_bp = Blueprint('unsubscribe', __name__)

@unsubscribe_bp.route('/api/unsubscribe', methods=['POST'])
def unsubscribe():
    data = request.json
    unsubscribe_url = data.get('unsubscribe_url')
    unsubscribe_mailto = data.get('unsubscribe_mailto')
    access_token = data.get('access_token')  # OAuth token

    if unsubscribe_url:
        try:
            resp = requests.get(unsubscribe_url, timeout=10)
            if resp.status_code in [200, 202, 204]:
                return jsonify({"status": "Unsubscribed successfully"})
            else:
                return jsonify({"error": f"Failed to unsubscribe, status code {resp.status_code}"}), 500
        except Exception as e:
            return jsonify({"error": f"Exception during unsubscribe: {str(e)}"}), 500

    elif unsubscribe_mailto:
        try:
            send_unsubscribe_email(access_token, unsubscribe_mailto)
            return jsonify({"status": "Unsubscribe email sent"})
        except Exception as e:
            return jsonify({"error": f"Failed to send unsubscribe email: {str(e)}"}), 500

    else:
        return jsonify({"error": "No unsubscribe method provided"}), 400
