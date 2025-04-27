from flask import Flask
import os

app = Flask(_name_)

@app.route('/')
def hello_world():
    return 'Hello hai!'

if _name_ == '_main_':
    # Ensuring the app runs on the correct port
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
