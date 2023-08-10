from flask import Flask, request, jsonify
import requests
from config import API_KEY, CSE_ID
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def exibir_imagem():
    return "kkkk nao sabe fazer pipoca. nao sabe nao sabe vai ter que aprender. orelha de burro cabeça de et. parece fácil !! mas é dificil :(( um belo dia vc vai ter que aprender....  BURRA!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
