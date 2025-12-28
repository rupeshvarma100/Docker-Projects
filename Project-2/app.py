from flask import Flask, jsonify, render_template, request, send_from_directory
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.before_request
def log_visitor():
    ip = request.remote_addr or 'unknown'
    r.lpush('recent_visitors', ip)
    r.ltrim('recent_visitors', 0, 99)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/api/stats')
def stats():
    visits = int(r.incr('visits'))
    r.expire('visits', 86400)
    users = r.scard('users')
    msg = r.get('welcome_msg') or 'Hello Docker Compose!'
    return jsonify({'visits': visits, 'users': users, 'message': msg})

@app.route('/api/users/<user_id>')
def track_user(user_id):
    r.sadd('users', user_id)
    return jsonify({'status': 'tracked'})

@app.route('/api/leaderboard')
def leaderboard():
    recent = r.lrange('recent_visitors', 0, 9)
    peak = int(r.get('peak_visits') or 0)
    current_visits = int(r.get('visits') or 0)
    if current_visits > peak:
        r.set('peak_visits', current_visits)
    return jsonify({'recent': recent, 'peak': peak})

# NEW: Clear endpoints
@app.route('/api/clear/visits')
def clear_visits():
    r.delete('visits', 'peak_visits')
    return jsonify({'status': 'visits cleared'})

@app.route('/api/clear/visitors')
def clear_visitors():
    r.delete('recent_visitors', 'users')
    return jsonify({'status': 'visitors cleared'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
