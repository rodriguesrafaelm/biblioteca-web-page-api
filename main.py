from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from controladores import *
import os


app = Flask(__name__)
cors = CORS(app)


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