from flask import Flask
from flask import request
from flask import render_template
import requests
import json
import sys
import time

import web3
from web3 import Web3, HTTPProvider, IPCProvider, utils

web3 = Web3(HTTPProvider("http://loanchain.org:443"))

app = Flask(__name__)
CAPITAL_ONE_KEY = "17f8e0c61ae537844b839d4b41309a6e" 

LOAN_ID = None

master_contract_address = None # SET THIS

def generate_smart_contract(amount, maturity):
    abi_raw = """ """
    abi = json.loads(abi_raw)
    bytecode = ""
    token_contract = web3.eth.contract(abi, bytecode=bytecode)
    tx_deploy_hash = token_contract.deploy(transaction={"from":web3.eth.accounts[0]})
    
    # wait for contract deployment transaction to be mined
    txn_receipt = web3.eth.getTransactionReceipt(tx_deploy_hash)
    while txn_receipt is None:
        time.sleep(1)
        txn_receipt = web3.eth.getTransactionReceipt(tx_deploy_hash) 
    
    contract_address = txn_receipt['contractAddress']
    my_contract = web3.eth.contract(abi=abi, address=contract_address)
    
    my_contract.transact().setloanterms(amount, maturity, master_contract_address)


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
    
    


    return render_template("complete.html")

if __name__ == "__main__":
    app.run()
