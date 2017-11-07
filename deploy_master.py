import sys
import time
import json

import web3
from web3 import Web3, HTTPProvider, IPCProvider, utils

print "Connecting to Blockchain.."
#web3 = Web3(HTTPProvider("https://ropsten.infura.io/7K9217xmVWshlCqJ49qG"))
web3 = Web3(HTTPProvider("http://loanchain.org:443"))
print "Conntected to Blockchain"
print ""

def generate_smart_contract():
    abi_raw = """[{"constant":false,"inputs":[],"name":"getrate","outputs":[{"name":"intrate","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_rate","type":"uint256"}],"name":"setrate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]"""
    abi = json.loads(abi_raw)
    bytecode = "6060604052341561000f57600080fd5b60d38061001d6000396000f3006060604052600436106049576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063520d3f0d14604e578063ba34c8f1146074575b600080fd5b3415605857600080fd5b605e6094565b6040518082815260200191505060405180910390f35b3415607e57600080fd5b60926004808035906020019091905050609d565b005b60008054905090565b80600081905550505600a165627a7a72305820363f920040ff0bbd6f22ca381b2d71617e1451e08317cde34560dbb00c696eb90029"    
    token_contract = web3.eth.contract(abi, bytecode=bytecode)
    tx_deploy_hash = token_contract.deploy(transaction={"from": "0xa5052689e2dbfff01bcb72bbbc8026f14b698d96"})
    print "Deploying Master Contract..."
    # wait for contract deployment transaction to be mined
    txn_receipt = web3.eth.getTransactionReceipt(tx_deploy_hash)
    while txn_receipt is None:
        print "..."
        time.sleep(1)
        txn_receipt = web3.eth.getTransactionReceipt(tx_deploy_hash)

    print("Deployed Contract")
    print("")

    contract_address = txn_receipt['contractAddress']

    my_contract = web3.eth.contract(abi=abi, address=contract_address)

    rate = float(sys.argv[1])

    print("Applying Interest Rate of " + str(rate))

    my_contract.transact({"from":"0xa5052689e2dbfff01bcb72bbbc8026f14b698d96"}).setrate(int(rate*1000))
    print "Rate Applied" 
    print "Master Address: " + str(contract_address)

if __name__ == "__main__":
    generate_smart_contract()

