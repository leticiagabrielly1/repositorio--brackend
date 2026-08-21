from flask import Flask, render_template

app = Flask(__name__)



def index():
    return render_template('index.html')


# 1. 
@app.route('/ola/<nome>')
def ola(nome):
    return render_template('ola.html', nome=nome)


# 2. 
@app.route('/calculo/<int:n1>/<int:n2>')
def calculo(n1, n2):
    soma = n1 + n2
    return render_template('calculo.html', n1=n1, n2=n2, soma=soma)


# 3. 
@app.route('/idade/<nome>/<int:idade>')
def idade(nome, idade):
    return render_template('idade.html', nome=nome, idade=idade)


# 4. 
@app.route('/produto/<nome>/<float:preco>')
def produto(nome, preco):
    return render_template('produto.html', nome=nome, preco=preco)


# 5. 
@app.route('/repetir/<palavra>/<int:vezes>')
def repetir(palavra, vezes):
    resultado = ' '.join([palavra] * vezes)
    return render_template('repetir.html', resultado=resultado)


# 3
@app.route('/arearestrita/<int:id>')
def arearestrita(id):
    if id == 1:
        return render_template(
            'arearestrita.html',
            mensagem='Acesso bloqueado',
            imagem='cadeado_fechado.svg'
        )
    elif id == 2:
        return render_template(
            'arearestrita.html',
            mensagem='Acesso liberado',
            imagem='cadeado_aberto.svg'
        )
    else:
        return render_template(
            'arearestrita.html',
            mensagem='ID inválido. Use 1 (bloqueado) ou 2 (liberado).',
            imagem=None
        )


# Questão 04
@app.route('/operacao/<tipo>/<op1>/<op2>')
def operacao(tipo, op1, op2):
    simbolos = {'sum': '+', 'sub': '-', 'mult': '*', 'div': '/'}

    try:
        op1 = float(op1)
        op2 = float(op2)
    except ValueError:
        return render_template('operacao.html', erro='op1 e op2 devem ser números.')

    if tipo == 'sum':
        resultado = op1 + op2
    elif tipo == 'sub':
        resultado = op1 - op2
    elif tipo == 'mult':
        resultado = op1 * op2
    elif tipo == 'div':
        if op2 == 0:
            return render_template('operacao.html', erro='Erro: divisão por zero.')
        resultado = op1 / op2
    else:
        return render_template(
            'operacao.html',
            erro='Tipo inválido. Use: sum, sub, mult ou div.'
        )

    return render_template(
        'operacao.html',
        op1=op1,
        op2=op2,
        simbolo=simbolos[tipo],
        resultado=resultado
    )


if __name__ == '__main__':
    app.run(debug=True)
