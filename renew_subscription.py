tx = contract.functions.renew(0).buildTransaction({
    "from": ACCOUNT.address,
    "value": w3.toWei(0.01, "ether"),
    "nonce": w3.eth.getTransactionCount(ACCOUNT.address),
    "gas": 100000
})
