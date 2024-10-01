from flask import Flask, jsonify, request
import google.generativeai as genai
import time

app = Flask(__name__)

api_key_google = "AIzaSyDQSTmWlMkGUTTKhjsdU4SIKw02zKyG9Cg"
genai.configure(api_key=api_key_google)
model = genai.GenerativeModel("gemini-1.5-pro-latest")


def format_text(text):
    # Replace occurrences of '*' with a newline followed by '*'
    formatted_text = text.replace('*', '\n*')
    return formatted_text

@app.route('/<nome_do_anime>')
def index(nome_do_anime):
    try:
        prompt = f"Me faça um resumo do personagem {nome_do_anime} do Harry Potter, colocando magias usadas nos livros, tipo de patrono, e a casa que ele pertence"
        response = model.generate_content(prompt)
        time.sleep(1)
        formatted_response = format_text(response.text)
        return formatted_response
    except Exception as e:
        app.logger.error(f"Erro ao processar a solicitação para {nome_do_anime}: {e}")
        return jsonify({"error": "Ocorreu um erro ao processar sua solicitação."}), 500


if __name__ == '__main__':
    app.run(debug=True)
