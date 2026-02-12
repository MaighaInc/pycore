from flask import Flask, jsonify, request

app = Flask(__name__)

# Valid API keys (in real app, store in database)
VALID_KEYS = ['sk-admin-key-123', 'sk-user-key-456']

def validate_api_key():
    """Check if request has valid API key"""
    api_key = request.headers.get('X-API-Key')
    return api_key in VALID_KEYS

# Public endpoint (no auth required)
@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({'status': 'API is running'}), 200

# Protected endpoint (requires API key)
@app.route('/api/admin/stats', methods=['GET'])
def admin_stats():
    if not validate_api_key():
        return jsonify({'error': 'Unauthorized. Provide X-API-Key header'}), 401
    
    stats = {
        'total_users': 1250,
        'total_products': 500,
        'api_calls_today': 45000
    }
    return jsonify(stats), 200

if __name__ == '__main__':
    app.run(debug=True)
