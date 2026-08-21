from flask import Flask, render_template

app = Flask(__name__)

# Dados de cada gênero: nome, imagem, descrição e cores do gradiente
generos = {
    'acao': {
        'nome': 'Ação',
        'imagem': 'acao.svg',
        'descricao': 'Filmes de ação trazem muita adrenalina, perseguições, '
                      'lutas e explosões, com um ritmo acelerado do início ao fim.',
        'cor1': '#c0392b',
        'cor2': '#e67e22',
    },
    'comedia': {
        'nome': 'Comédia',
        'imagem': 'comedia.svg',
        'descricao': 'Filmes de comédia têm como objetivo divertir o público, '
                      'trazendo situações engraçadas e diálogos leves.',
        'cor1': '#f39c12',
        'cor2': '#f1c40f',
    },
    'terror': {
        'nome': 'Terror',
        'imagem': 'terror.svg',
        'descricao': 'Filmes de terror buscam causar medo e tensão no espectador, '
                      'geralmente com elementos sobrenaturais ou psicológicos.',
        'cor1': '#2c3e50',
        'cor2': '#8e44ad',
    },
    'romance': {
        'nome': 'Romance',
        'imagem': 'romance.svg',
        'descricao': 'Filmes de romance exploram relações amorosas e emoções, '
                      'focando na conexão entre os personagens.',
        'cor1': '#e91e63',
        'cor2': '#f8bbd0',
    },
}

genero_nao_encontrado = {
    'nome': 'Gênero não disponível',
    'imagem': 'nao_encontrado.svg',
    'descricao': 'O gênero informado não foi encontrado em nosso catálogo. '
                  'Tente: acao, comedia, terror ou romance.',
    'cor1': '#7f8c8d',
    'cor2': '#bdc3c7',
}


@app.route('/')
def index():
    return render_template('index.html', generos=generos)


@app.route('/filme/<genero>')
def filme(genero):
    dados = generos.get(genero, genero_nao_encontrado)
    return render_template(
        'filme.html',
        nome=dados['nome'],
        imagem=dados['imagem'],
        descricao=dados['descricao'],
        cor1=dados['cor1'],
        cor2=dados['cor2'],
    )


if __name__ == '__main__':
    app.run(debug=True)