
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Você pode definir a data de lançamento aqui e passar para o template se desejar
    return ('index.html')

if __name__ == '__main__':
    app.run(debug=True)