from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Eduardo'}
    data = ['29/12/2019', '20/12/2019']
    texto = ['blablablabla',
             'faltam loop e herança de template para completar a parte 2'
             ]
    versao = ['1.0.2v', '1.0.1v']
    link = ['a','https://github.com/edumangabeira/python_exercicios/commit/cf1b5d8575f53cac28822ca2b9ac49dc8fa0b1da']
    posts = [{
        'data': data[0],
        'versao': versao[0],
        'texto': texto[0],
        'link': link[0]
    },
        {
        'data': data[1],
        'versao': versao[1],
        'texto': texto[1],
        'link': link[1]
    }
    ]
    return render_template('index.html', user=user, posts=posts)
