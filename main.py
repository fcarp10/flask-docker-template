from flask import Flask
import os


app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello world!'


if __name__ == '__main__':
    if os.getenv('ENVIRONMENT') != 'production':
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        app.run(host='0.0.0.0', port=80, debug=False)
