# Importando o Flask, render template, request e Tinker

from flask import Flask, render_template

app = Flask(__name__)

# Criando a página no site

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/games')
def games_page():
    return render_template('games.html')

@app.route('/categories/<game_category>')
def categories(game_category):
    return render_template('game_category.html', game_category = game_category)

# Colocando o site no ar

if __name__ == '__main--':
    app.run(debug = True)

# Servidor do Heroku

# requirements.txt

app.run()
