from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/')
def assinatura():
    return render_template('assinatura.html')

@app.route('/')
def contato():
    return render_template('contato.html')

@app.route('/')
def meuPerfil():
    return render_template('meuPerfil.html')

@app.route('/')
def favoritos():
    return render_template('favoritos.html')

@app.route('/')
def cadastro():
    return render_template('cadastro.html')

@app.route('/')
def cursos():
    return render_template('cursoss.html')

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/')
def pagamento():
    return render_template('pagamento.html')


if __name__ == '__main__':
    app.run(debug=True)
