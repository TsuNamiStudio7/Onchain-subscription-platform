tx = contract.functions.cancel(0).buildTransaction({
    "from": ACCOUNT.address,
    "nonce": w3.eth.getTransactionCount(ACCOUNT.address),
    "gas": 80000
})
