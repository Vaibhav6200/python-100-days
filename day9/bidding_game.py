import os

print("Welcome to the secret auction program.")


auction = {}


def find_highest_bidder():
    winner_name = ""
    winner_bid = 0
    for key in auction:
        if auction[key] > winner_bid:
            winner_bid = auction[key]
            winner_name = key
    print(f"The winner is {winner_name} with a bid of ${winner_bid}")



bidding_finished = False
while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    auction[name] = bid

    answer = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if answer == 'no':
        find_highest_bidder()
        bidding_finished = True
    elif answer == 'yes':
        os.system('cls')
    else:
        print("Invalid input.\n")


