from config import w3, ACCOUNT

def send_transaction(tx):
    signed_tx = w3.eth.account.signTransaction(tx, ACCOUNT.privateKey)
    return w3.eth.sendRawTransaction(signed_tx.rawTransaction)
