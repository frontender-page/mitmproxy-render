from flask import Flask
import threading
import time

app = Flask(__name__)

@app.route('/ping')
def ping():
    return "pong", 200

@app.route('/')
def home():
    return "OK", 200

if __name__ == '__main__':
    # Запускаем на порту 8081 (Render автоматически обнаружит его)
    app.run(host='0.0.0.0', port=8081)
