from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
PRIVATE_KEY = "0xYourPrivateKey"
ACCOUNT = w3.eth.account.privateKeyToAccount(PRIVATE_KEY)
