import os
from flask import Flask, request, jsonify
from langchain_chatbot.controller import build_respose


# Definning app
app = Flask(__name__)


# chatbot end-point
@app.route('/chatbot', methods=['POST'])
def chatbot():

    #Getting data
    data = request.get_json()
    query = data.get("query", "")
    context = data.get("context", "")

    if not query: raise Exception("No query provided")
    if not context: raise Exception("No context provided")

    # Processing
    response = build_respose(context, query)

    return jsonify({"response", response.content})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
