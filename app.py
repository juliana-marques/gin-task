from flask import Flask, request, jsonify
import requests
from config import API_KEY, CSE_ID
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def exibir_imagem():
    return "oi"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
