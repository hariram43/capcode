from flask import Flask, jsonify
import boto3
from werkzeug.exceptions import NotFound

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
[root@ip-172-31-84-47 sample-app]# cat hello.py
from flask import Flask, jsonify
import boto3
from werkzeug.exceptions import NotFound

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
