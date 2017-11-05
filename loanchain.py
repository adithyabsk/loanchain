from flask import Flask
from flask import request
from flask import render_template
import requests
import json
import sys

app = Flask(__name__)
CAPITAL_ONE_KEY = "17f8e0c61ae537844b839d4b41309a6e" 

LOAN_ID = None

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/bank/')
def bank():
    input_default = ""
    input_disabled = None
    rslt_hidden = "hidden"
    submit_disabled = None
    result = ""
    return render_template("bank.html", **locals())

@app.route('/bank/getLoan', methods=['POST'])
def get_loan():
    res = None
    try:
        url = "http://api.reimaginebanking.com/loans/{}?key={}".format(request.form["id"], CAPITAL_ONE_KEY)
        res = requests.get(url)
    except Exception as e:
        error = str(e.message)+'\n'
        sys.stderr.write(error)
        api_error_message = error
        return render_template("bank.html", api_get_successful=False, **locals())
    
    input_default = str(request.form["id"])
    LOAN_ID = input_default
    input_disabled = "disabled"
    hide_result = None
    submit_disabled = "disabled"

    data = json.loads(res.content) 
    name  = data["description"]
    amount = data["amount"]

    return render_template("bank.html", api_get_successful=True, **locals())

@app.route('/bank/gatherMoreLoanData', methods=['POST'])
def gather_more_loan_data():
    data = request.form
    # Make a post here and pass data
    return render_template("complete.html")
    
@app.route('/bank/postToBlockChain', methods=['POST'])
def post_to_blockchain():
    pass


if __name__ == "__main__":
    app.run()
