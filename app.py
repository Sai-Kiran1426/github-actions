from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello hai!'

if __name__ == '__main__':
    # Ensuring the app runs on the correct port
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
