from flask import  Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Você está na página inicial do site'

@app.route('/pagina_contatos')
def contatos():
    return 'qualquer dúvida ligue para esse número (88) 999315675'

if __name__ == '__main__':
    app.run(debug=True)
