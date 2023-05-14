from flask import Flask, jsonify, send_from_directory, request, redirect, url_for
from flask_httpauth import HTTPBasicAuth
from os import getenv
import openai
import json

AUTH = getenv('AUTH') != '0'
PORT = int(getenv('PORT'))
TOKEN = getenv('TOKEN')
USERS = open('users.json','r').read()

openai.api_key = TOKEN
users = json.loads(USERS)

app = Flask(__name__, static_folder='public')
auth = HTTPBasicAuth()



@auth.verify_password
def auth_user(username, password):
    if username in users and password==users.get(username):
        return True

def auth_wrap(func):
    def wrapper():
        if AUTH:
            return auth.login_required(func)()
        else:
            return func()
    return wrapper

@app.before_request
@auth_wrap
def auth_all_requests():
    pass

@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))


@app.route('/<path:path>')
def send_file(path):
    return send_from_directory('public', path)

@app.route('/get-prompt-result', methods=['POST'])
def get_prompt_result():
    jsonObj = request.get_json()
    modelSelect = jsonObj.get('model')
    model = "gpt-3.5-turbo"
    if modelSelect == 'chatgpt':
        model = "gpt-3.5-turbo"
    if modelSelect == 'gpt':
        model = "davinci"
    if modelSelect == 'codex':
        model = "code-davinci-002"
    if modelSelect == "gpt-4":
        model = "gpt-4"

    msg = jsonObj.get('messages')
    print(msg, model, flush=True)
    response = openai.ChatCompletion.create(
        model=model,
        messages=msg
    )
    print(response['choices'][0]['message']['content'])
    return response['choices'][0]['message']['content']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
