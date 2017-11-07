import sys
import time
import json

import web3
from web3 import Web3, HTTPProvider, IPCProvider, utils

print "Connecting..."
#web3 = Web3(HTTPProvider("https://ropsten.infura.io/7K9217xmVWshlCqJ49qG"))
web3 = Web3(HTTPProvider("http://loanchain.org:443"))
print "Connected to Blockchain"
print ""
def generate_smart_contract():

    abi_raw = """[{"constant":false,"inputs":[],"name":"calcinterest","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"makepayment","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"viewbalance","outputs":[{"name":"remainingbalance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"_total","type":"uint256"},{"name":"_maturity","type":"uint256"},{"name":"_ratesource","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]"""
    abi = json.loads(abi_raw)
    bytecode="60606040526000600960006101000a81548160ff0219169083151502179055506000600a60146101000a81548160ff021916908315150217905550612710600b556000600d60006101000a81548160ff0219169083151502179055506000600e556000600f55341561007057600080fd5b60405160608061040c833981016040528080519060200190919080519060200190919080519060200190919050506000336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550826004819055508360028190555081600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1690508073ffffffffffffffffffffffffffffffffffffffff1663520d3f0d6000604051602001526040518163ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401602060405180830381600087803b15156101c057600080fd5b6102c65a03f115156101d157600080fd5b505050604051805190506006819055506000600581905550600060108190555050505050610208806102046000396000f300606060405260043610610062576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680630df4f38e146100675780631de9fa061461007c5780633ccfd60b14610086578063af61ed3d1461009b575b600080fd5b341561007257600080fd5b61007a6100c4565b005b6100846101ae565b005b341561009157600080fd5b6100996101d0565b005b34156100a657600080fd5b6100ae6101d2565b6040518082815260200191505060405180910390f35b600080600080600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1693508373ffffffffffffffffffffffffffffffffffffffff1663520d3f0d6000604051602001526040518163ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401602060405180830381600087803b151561015b57600080fd5b6102c65a03f1151561016c57600080fd5b505050604051805190506006819055506005925082600654600b54010a915082600b540a90508082600254028115156101a157fe5b0460028190555050505050565b3460026000828254039250508190555034600560008282540192505081905550565b565b60006002549050905600a165627a7a723058206666f122280dfde29192100c0137128b7b7d2dcd11aab8cb9d034c96f888fee30029"
    token_contract = web3.eth.contract(abi, bytecode=bytecode)
    tx_deploy_hash = token_contract.deploy(transaction={"from":"0xa5052689e2dbfff01bcb72bbbc8026f14b698d96"},args=[100,200,str(sys.argv[1])])
    
    print "Deploying loan... (Amount: 100 eth / Maturity: 200 months)"
    # wait for contract deployment transaction to be mined
    txn_receipt = web3.eth.getTransactionReceipt(tx_deploy_hash)
    while txn_receipt is None:
        time.sleep(1)
	print("...")
        txn_receipt = web3.eth.getTransactionReceipt(tx_deploy_hash)

    contract_address = txn_receipt['contractAddress']
    print contract_address
    my_contract = web3.eth.contract(abi=abi, address=contract_address)

    print  "Loan Deployed"
    print ""


    balance = my_contract.call({"from":"0xa5052689e2dbfff01bcb72bbbc8026f14b698d96"}).viewbalance()
    print "Current Loan Balance: " + str(balance)
    print ""

    loanhash = my_contract.transact({"from":"0xa5052689e2dbfff01bcb72bbbc8026f14b698d96"}).calcinterest()

    print("Calculating Interest.... (Pulling rate from master)")
    txn_receipt = web3.eth.getTransactionReceipt(loanhash)
    while txn_receipt is None:
        time.sleep(1)
	print("...")
        txn_receipt = web3.eth.getTransactionReceipt(loanhash)

    print("Interest Calculated")
    print("")
    #print(txn_receipt)


    balance = my_contract.call({"from":"0xa5052689e2dbfff01bcb72bbbc8026f14b698d96"}).viewbalance()
    print "Current Balance: " + str(balance)
    print ""
    payhash = my_contract.transact({"from":"0xa5052689e2dbfff01bcb72bbbc8026f14b698d96","value":100}).makepayment()


    print("Making Loan Payment... (100 eth)")
    txn_receipt = web3.eth.getTransactionReceipt(payhash)
    while txn_receipt is None:
        time.sleep(1)
	print("...")
        txn_receipt = web3.eth.getTransactionReceipt(payhash)

    print "Payment Complete"
    print ""


    balance = my_contract.call({"from":"0xa5052689e2dbfff01bcb72bbbc8026f14b698d96"}).viewbalance()
    print "Balance: " + str(balance)
    print ""

    print "DEMO COMPLETE *Mic Drop*"
    


if __name__ == "__main__":
    generate_smart_contract()


