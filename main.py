from flask import  Flask, render_template

app = Flask(__name__)

lista_usuarios = ['Lira', 'João', 'Alon', 'Alessandra', 'Amanda', 'Saulo']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pagina_contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios= lista_usuarios)

if __name__ == '__main__':
    app.run(debug=True)
