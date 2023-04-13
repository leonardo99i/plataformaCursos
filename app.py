from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/assinatura')
def assinatura():
    return render_template('assinatura.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/meuPerfil')
def meuPerfil():
    return render_template('meuPerfil.html')

@app.route('/favoritos')
def favoritos():
    return render_template('favoritos.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cursos')
def cursos():
    return render_template('cursoss.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/pagamento')
def pagamento():
    return render_template('pagamento.html')


if __name__ == '__main__':
    app.run(debug=True)
