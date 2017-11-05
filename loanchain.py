from flask import Flask
from flask import request
from flask import render_template
import reqeusts

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/bank/')
def bank():
    return render_template("bank.html")

@app.route('/bank/', methods=['POST'])
def bank_post():
    text = request.form['text']
    processed_text = text.upper()

    return processed_text

if __name__ == "__main__":
    app.run()
