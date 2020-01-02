import os
import yaml
import requests, json, random
from flask import Flask, jsonify, request, render_template, Response

from cats.cats import get_cat_images, get_cats_info


app = Flask(__name__)

@app.route('/')
def index():
    return "♥ ❤ ♥ Cabritinha ♥ ❤ ♥"

@app.route('/health', methods=['GET'])
def health():
    response = {"status":"ok"}
    return jsonify(response)

@app.route('/api/cats', methods=['POST', 'GET'])
def fetch_cats_info():
    cat_facts = get_cats_info()
    return jsonify(cat_facts)

@app.route('/api/cats/images', methods=['GET'])
def get_images():
    cat_image = get_cat_images('d336bdee-3fd9-4afc-aa84-ae9b2a0635fb')[0]['url']
    return render_template('cats.html', cat_img=cat_image)

@app.route('/api/error/500', methods=['POST'])
def generate_error():
    error_message = {'Error' : 'This is an example'}
    return Response(str(error_message), status=500, mimetype='application/json')
    

if __name__ == '__main__':
    #Host resposavel para servir o trafego alem do localhost
    app.run(debug=True, host='0.0.0.0', port=8080)
