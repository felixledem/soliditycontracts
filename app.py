from web3 import Web3, HTTPProvider
from solc import compile_files

web3 = Web3(HTTPProvider('http://localhost:8545'))


def deploy_contract():
    # get accounts
    accounts = web3.eth.accounts

    # contract stuff
    contract = compile_files(['./dragonstone.sol']).popitem()[1]
    abi = contract.get('abi')
    bytecode = contract.get('bin')
    web3_contract = web3.eth.contract(abi=abi, bytecode=bytecode)
    transaction = {'from': accounts[0], 'gas': 500000}
    trans_hash = web3_contract.deploy(transaction=transaction)
    txn_receipt = web3.eth.getTransactionReceipt(trans_hash)
    contract_address = txn_receipt['contractAddress']
    instance = web3_contract.call({'to': contract_address})
    i = instance.create(accounts[1], 1*10**18)
    print(web3.eth.getBalance(accounts[0]))
    print(web3.eth.getBalance(accounts[1]))

if __name__ == "__main__":
    deploy_contract()
