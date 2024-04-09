# app.py
from flask import Flask, render_template, request, jsonify
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

languages = {
    'Python': 0,
    'JavaScript': 0,
    'Java': 0,
    'C++': 0,
    'Go': 0
}

@app.route('/')
def index():
    return render_template('index.html', languages=languages)

@app.route('/vote', methods=['POST'])
def vote():
    language = request.json['language']
    if language in languages:
        redis_client.incr(language)
        languages[language] += 1
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': 'Invalid language'})

@app.route('/results')
def results():
    language_votes = {lang.decode(): int(redis_client.get(lang)) for lang in languages.keys()}
    sorted_votes = sorted(language_votes.items(), key=lambda x: x[1], reverse=True)
    return render_template('results.html', sorted_votes=sorted_votes)

if __name__ == '__main__':
    app.run(debug=True)
