#from flask import Flask, render_template
from flask import*
import random

app = Flask(__name__)

@app.route('Pagina principal')
def pag1():
    return render_template('pag1.html')

@app.route('Pagina secundaria')
def pag2():
    return render_template('pag2.html')

@app.route('Pagina terciaria')
def pag3():
    return render_template('pag3.html')

if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = random.randint (2000,9000)
    )