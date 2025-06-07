from flask import Flask, render_template, request, jsonify
from chatbot import responder

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get('mensagem')
    resposta = responder(user_msg)
    return jsonify({'resposta': resposta})

if __name__ == '__main__':
    app.run(debug=True)


def responder(msg):
    msg = msg.lower()
    if "projeto" in msg:
        return "Você pode ver meus projetos na aba 'Projetos'."
    elif "contato" in msg:
        return "Você pode me mandar mensagem pela aba 'Contato'."
    elif "nome" in msg:
        return "Meu nome é CoronelBot, prazer! 🤖"
    else:
        return "Desculpe, não entendi muito bem. Pode tentar de outra forma?"
