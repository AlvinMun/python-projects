from art import logo
print(logo)

def find_highest(record):
    highest_bid = 0
    winner = ""
    for key in record:
        amount = record[key]
        if amount > highest_bid:
            highest_bid = amount
            winner = key
    print(f"The winner is {winner} with a bid of ${highest_bid}")

auction = {}
should_continue = True
while should_continue:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    yes_or_no = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    auction[name] = bid
    if yes_or_no == 'yes':
        print("\n" * 100)
        continue
    if yes_or_no == 'no':
        should_continue = False
        find_highest(auction)
