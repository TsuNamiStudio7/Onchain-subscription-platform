from config import w3, ACCOUNT
import json

with open("SubscriptionPlatform_abi.json") as f:
    abi = json.load(f)

bytecode = "0x..."  # Replace with compiled bytecode

Contract = w3.eth.contract(abi=abi, bytecode=bytecode)
tx = Contract.constructor().buildTransaction({
    "from": ACCOUNT.address,
    "nonce": w3.eth.getTransactionCount(ACCOUNT.address),
    "gas": 3000000
})

from wallet_utils import send_transaction
tx_hash = send_transaction(tx)
print("Deployed at tx:", w3.toHex(tx_hash))
