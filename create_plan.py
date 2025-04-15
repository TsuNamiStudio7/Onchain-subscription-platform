from config import w3, ACCOUNT
from wallet_utils import send_transaction
import json

with open("SubscriptionPlatform_abi.json") as f:
    abi = json.load(f)

contract_address = "0x..."  # Replace with deployed address
contract = w3.eth.contract(address=contract_address, abi=abi)

tx = contract.functions.createPlan(
    w3.toWei(0.01, "ether"), 86400 * 30  # 30 days
).buildTransaction({
    "from": ACCOUNT.address,
    "nonce": w3.eth.getTransactionCount(ACCOUNT.address),
    "gas": 100000
})

tx_hash = send_transaction(tx)
print("Plan created:", w3.toHex(tx_hash))
