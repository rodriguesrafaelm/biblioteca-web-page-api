from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from controladores import *
import os

import json


app = Flask(__name__)
cors = CORS(app)

'''@app.route("/livros", methods=['GET', 'POST', 'DELETE'])
def livros():
    if request.method == 'GET':
        objetos = []
        books_db = listar()
        for livro in books_db:
            a = {'id':livro[0], 'livro':livro[1], 'autor' : livro[2], 'ano_publicado' : livro[3], 'editora' : livro[4], 'image_url' : livro[5]}
            objetos.append(a)
        return jsonify(objetos)
    if request.method == 'POST':
        data = request.get_data().decode('utf-8')
        data = json.loads(data)
        add_livro(data['nome'], data['autor'])
        return '200'
    if request.method == 'DELETE':
        data = request.get_data()
        data = json.loads(data)
        id = data['id_livro']
        remover_livro(id)
        return '200''''


@app.route("/livros/<id>", methods=['GET'])
def book_by_id(id):
    if selecionar_livro(id):
        livro = selecionar_livro(id)
        a = {'id':livro[0], 'livro':livro[1], 'autor' : livro[2], 'ano_publicado' : livro[3], 'editora' : livro[4], 'image_url' : livro[5]}
        return a
    else:
        return 'Livro não encontrado'

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSON_AS_ASCII'] = False
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)