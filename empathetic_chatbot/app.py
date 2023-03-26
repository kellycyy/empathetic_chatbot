from flask import Flask, request, render_template, jsonify
from trying_langchain import get_response
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    input_text = request.form['text']
    print(input_text)
    response = generate_response(input_text)
    return jsonify({'response': response})

def generate_response(input_text):
    return get_response(input_text)

if __name__ == '__main__':
    app.run(debug=True)
