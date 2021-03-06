import sys
import json
import requests
import web3
from web3 import Web3, HTTPProvider, IPCProvider, utils

web3 = Web3(HTTPProvider("http://loanchain.org:443"))

master_contract_address = None
master_contract_bytecode = "606060405260606040519081016040528073ca35b7d915458ef540ade6068dfe2f44e8fa733c73ffffffffffffffffffffffffffffffffffffffff168152602001738d7d242d87fb67ad22bfcf0e4d10933d4dc8f70073ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200173770a05a923d2f22603cc1897660963d1b078b73173ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681525060009060036100da9291906100eb565b5034156100e657600080fd5b6101b8565b828054828255906000526020600020908101928215610164579160200282015b828111156101635782518260006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055509160200191906001019061010b565b5b5090506101719190610175565b5090565b6101b591905b808211156101b157600081816101000a81549073ffffffffffffffffffffffffffffffffffffffff02191690555060010161017b565b5090565b90565b61017f806101c76000396000f30060606040526004361061004c576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063520d3f0d14610051578063ba34c8f11461007a575b600080fd5b341561005c57600080fd5b61006461009d565b6040518082815260200191505060405180910390f35b341561008557600080fd5b61009b60048080359060200190919050506100a7565b005b6000600154905090565b60008060009150600090505b600080549050811015610140573373ffffffffffffffffffffffffffffffffffffffff166000828154811015156100e657fe5b906000526020600020900160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16141561013357600191505b80806001019150506100b3565b811561014e57826001819055505b5050505600a165627a7a72305820c6a213b35c7fc2a46f741e5ea559e9159cc459c290dffd9f7af81c9633fbc2030029"

def getTreasury():
    res = None
    try:
        url = "https://www.xignite.com/xRates.json/GetRate?RateType=TreasuryConstant1Year&AsOfDate=11/3/2017&_token=628C637E699240CC91C99F79BFE6F1CB"
        res = requests.get(url)
    except Exception as e:
        return 0

    return json.loads(res.content)["Value"]

def updateRates():
    treasury = getTreasury()
    master_contract = web3.eth.contract(address=master_contract__address, bytecode=master_contract_bytecode)
    master_contract.transact().setrate(treasury*1000)

if __name__ == "__main__":
   updateRates()
   print "Updated Treasury Rates"


