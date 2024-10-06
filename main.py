import os
from flask import Flask, request, jsonify


# Definning app
app = Flask(__name__)


# chatbot end-point
@app.route('/chatbot', methods=['POST'])
def chatbot():
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
