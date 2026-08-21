from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        return f'Usuário "{usuario}" enviado com sucesso.'
    return render_template('login.html')



@app.route('/alunos')
def alunos():
    lista_alunos = [
        {'nome': 'Alice', 'matricula': '12345678'},
        {'nome': 'Bruno', 'matricula': '86123962'},
        {'nome': 'Clara', 'matricula': '27167398'},
        {'nome': 'Maridson', 'matricula': '38271612'},
        {'nome': 'Valéria', 'matricula': '75826163'},
    ]
    return render_template('alunos.html', alunos=lista_alunos)


if __name__ == '__main__':
    app.run(debug=True)