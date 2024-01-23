import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return f"Name: {os.getenv('NAME', 'DefaultName')}\nPosition: {os.getenv('POSITION', 'DefaultPosition')}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=81)
