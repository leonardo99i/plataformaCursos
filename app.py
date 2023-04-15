from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Verificar credenciais de login
        # Se as credenciais estiverem corretas, redirecionar para a página home
        return redirect(url_for('home'))
    else:
        return render_template('login.html')

@app.route('/home')
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

@app.route('/pagamento', methods=['GET', 'POST'])
def pagamento():
    if request.method == 'POST':
        # Verificar pagamento
        # Se o pagamento estiver confirmado, redirecionar para a página de login
        return redirect(url_for('login'))
    else:
        return render_template('pagamento.html')

if __name__ == '__main__':
    app.run(debug=True)

