from flask import render_template
from flask_socketio import SocketIO, emit
import redis

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

languages = {
    'Python': 'python_votes',
    'JavaScript': 'javascript_votes',
    'Java': 'java_votes',
    'C++': 'cpp_votes',
    'Go': 'go_votes'
}

@app.route('/')
def index():
    language_votes = {}
    for language, key in languages.items():
        vote_count_bytes = redis_client.get(key)
        vote_count = int(vote_count_bytes.decode()) if vote_count_bytes is not None else 0
        language_votes[language] = vote_count
    return render_template('index.html', language_votes=language_votes)

@app.route('/results')
def results():
    language_votes = {}
    for language, key in languages.items():
        vote_count_bytes = redis_client.get(key)
        vote_count = int(vote_count_bytes.decode()) if vote_count_bytes is not None else 0
        language_votes[language] = vote_count
    sorted_votes = sorted(language_votes.items(), key=lambda x: x[1], reverse=True)
    return render_template('results.html', sorted_votes=sorted_votes)

@app.route('/vote', methods=['POST'])
def vote():
    language = request.json['language']
    if language in languages:
        redis_key = languages[language]
        redis_client.incr(redis_key)
        new_count = int(redis_client.get(redis_key).decode())
        socketio.emit('vote_update', {'language': language, 'count': new_count}, broadcast=True)
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': 'Invalid language'})

if __name__ == '__main__':
    socketio.run(app, debug=True)
