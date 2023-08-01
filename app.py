from flask import Flask, request, jsonify
import requests
from config import API_KEY, CSE_ID
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def exibir_imagem():
    search_query = 'gato programando'

    url = f"https://customsearch.googleapis.com/customsearch/v1?cx={CSE_ID}&key={API_KEY}&q={search_query}&imgType=animated&searchType=image"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        items = data.get('items', [])
        if items:
            random_index = random.randint(0, len(items) - 1)
            random_item = items[random_index]
            image_url = random_item['link']
            return f'<img src="{image_url}" alt="Imagem" style="max-width: 300px; max-height: 300px; margin: auto;"> + Hello Cats!'


        else:
            return jsonify({'error': 'Nenhum resultado encontrado.'})

    except requests.exceptions.HTTPError as err:
        return jsonify({'error': f"Erro na solicitação da API: {err}"})
    except requests.exceptions.RequestException as err:
        return jsonify({'error': f"Erro ao fazer a solicitação: {err}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
