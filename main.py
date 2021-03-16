'''
    Name: main.py
    Writer: Hoseop Lee, Ainizer
    Rule: Flask app server
    update: 21.01.27
'''

from flask import Flask, request, jsonify, render_template
import requests
import json


app = Flask(__name__)


##
# Get post request page.
@app.route('/SpongeBob', methods=['POST'])
def generate():
    try:
        name = request.form['name']
        text = request.form['text']
        length = int(request.form['length'])
        URL = 'https://feature-add-torch-serve-gpt-2-server-gkswjdzz.endpoint.ainize.ai/infer/gpt2-Spongebob50'
        headers = {
            'Content-Type': 'application/json'
        }
        res = requests.post(URL, headers=headers, data=json.dumps({
            'text': f'{name}: {text}',
            'num_samples': 1,
            'length': length
        }))

        print(res.text)
        sample_outputs = res.json()

        result = []
        friends_stories = sample_outputs['0'].split('\n')

        for idx, friends_story in enumerate(friends_stories):
            if idx == len(friends_stories) - 1:
                break
            if friends_story and ': ' in friends_story:
                    splitted = friends_story.split(':')
                    print(splitted[0],splitted[1])
                    result.append([splitted[0], splitted[1]])
            else:
                continue

        return jsonify({0: result}), 200
    except Exception as e:
        return jsonify({'message': e}), 500


##
# Sever health checking page.
@app.route('/healthz', methods=["GET"])
def health_check():
    return "Health", 200


##
# Main page.
@app.route('/')
def main():
    return render_template('main.html'), 200


if __name__ == '__main__':
    app.run(port=80, host='0.0.0.0')
