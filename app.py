from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is a CI/CD demo.'

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)