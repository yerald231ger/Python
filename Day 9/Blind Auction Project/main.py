# TODO-1: Ask the user for input
import os
import subprocess
import sys

print("Welcome to the secret auction program.")
bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("Whats your name?: ")
    price = int(input("Whats your bid?: $"))

    bids[name] = price

    print("\n" * 100)
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if should_continue == "no":
        bidding_finished = True
        highest_bid = 0
        winner = ""

        for bidder in bids:
            if bids[bidder] > highest_bid:
                highest_bid = bids[bidder]
                winner = bidder
        print(f"The winner is {winner} with a bid of ${highest_bid}")

