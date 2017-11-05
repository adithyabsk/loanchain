from time import sleep
import web3
import sys
from web3 import Web3, HTTPProvider, IPCProvider, utils

web3 = Web3(HTTPProvider("http://loanchain.org:443"))

#def new_transaction_callback(transaction_hash):
#    print("Test")
#    print("New Block: {0}".format(transaction_hash))

#new_transaction_filter = web3.eth.filter('pending')
#new_transaction_filter.watch(new_transaction_callback)

def new_block_callback(block_hash):
    print("New Block")
    print(web3.eth.getTransactionCount('latest'))

new_block_filter = web3.eth.filter('latest')
new_block_filter.watch(new_block_callback)


while True: sleep(1)

# each time the client receieves a unmined transaction the
# `new_transaction_filter` function will be called with the transaction
# hash. 
