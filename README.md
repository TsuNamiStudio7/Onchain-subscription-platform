# Onchain Subscription Platform

Decentralized subscription service for creators and users.

## Features

- Multiple plans by different creators
- Manual renewal
- Real ETH payments onchain
- Verifiable status

## Files

- Smart Contract: `SubscriptionPlatform.sol`
- ABI: `SubscriptionPlatform_abi.json`
- Deploy script: `deploy_contract.py`
- Plan management: `create_plan.py`
- User interaction: `subscribe_user.py`, `renew_subscription.py`, `cancel_subscription.py`, `check_subscription_status.py`

## How it Works

1. Deploy contract
2. Creator creates a plan (price + duration)
3. User subscribes to plan
4. User can renew or cancel
5. Creator gets paid immediately

## Testable with Ganache + Web3.py
