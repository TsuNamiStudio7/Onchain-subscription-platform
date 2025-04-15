from config import w3, ACCOUNT
from wallet_utils import send_transaction
import json

with open("SubscriptionPlatform_abi.json") as f:
    abi = json.load(f)

contract_address = "0xYourDeployedContractAddress"
contract = w3.eth.contract(address=contract_address, abi=abi)

def test_create_plan():
    tx = contract.functions.createPlan(w3.toWei(0.01, 'ether'), 30).buildTransaction({
        "from": ACCOUNT.address,
        "nonce": w3.eth.getTransactionCount(ACCOUNT.address),
        "gas": 100000
    })
    tx_hash = send_transaction(tx)
    print("✅ Plan created:", w3.toHex(tx_hash))

def test_subscribe():
    tx = contract.functions.subscribe(0).buildTransaction({
        "from": ACCOUNT.address,
        "value": w3.toWei(0.01, 'ether'),
        "nonce": w3.eth.getTransactionCount(ACCOUNT.address),
        "gas": 100000
    })
    tx_hash = send_transaction(tx)
    print("✅ Subscribed:", w3.toHex(tx_hash))

def test_is_active():
    active = contract.functions.isActive(ACCOUNT.address, 0).call()
    print("📦 Subscription active:", active)

if __name__ == "__main__":
    test_create_plan()
    test_subscribe()
    test_is_active()
