SubscriptionPlatform.sol// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SubscriptionPlatform {
    struct Plan {
        uint256 price;
        uint256 duration; // in seconds
        address creator;
    }

    struct Subscription {
        uint256 expiry;
        bool active;
    }

    mapping(uint256 => Plan) public plans;
    mapping(address => mapping(uint256 => Subscription)) public subscriptions;
    uint256 public planCount;

    function createPlan(uint256 price, uint256 duration) public {
        plans[planCount] = Plan(price, duration, msg.sender);
        planCount++;
    }

    function subscribe(uint256 planId) public payable {
        Plan memory plan = plans[planId];
        require(msg.value >= plan.price, "Insufficient payment");

        subscriptions[msg.sender][planId] = Subscription(
            block.timestamp + plan.duration,
            true
        );

        payable(plan.creator).transfer(plan.price);
    }

    function renew(uint256 planId) public payable {
        Plan memory plan = plans[planId];
        require(msg.value >= plan.price, "Insufficient payment");

        Subscription storage sub = subscriptions[msg.sender][planId];
        require(sub.active, "Not subscribed");

        if (sub.expiry < block.timestamp) {
            sub.expiry = block.timestamp + plan.duration;
        } else {
            sub.expiry +=
