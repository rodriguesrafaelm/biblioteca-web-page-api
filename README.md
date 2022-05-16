
# Rotas:<br>

##### [GET] URL/livros/id -> Retorna um livro com o ID correspondente ao valor de "id". Caso não exista, retorna mensagem 'Livro não encontrado'.<br>

Disponivel no Heroku: https://using-api-to-learn.herokuapp.com/livros/ID <br>
Substituir o ID na URL por um numero entre 1 e 271379 <br><br>

Essa API foi utilizada nesse projeto -> https://github.com/rodriguesrafaelm/biblioteca-web-page
<br><br><br>
O arquivo [data_colector.py](https://github.com/rodriguesrafaelm/biblioteca-web-page-api/blob/main/data_collector.py) é um pequeno script que usando pandas e sqlite3 Copia dados especificos do dataset para um banco de dados SQL.<br>
Utilizei SQLite por se tratar de um projeto simples e por estar apenas praticando.
