bidders = {}
while True:
    name = input("What is your name? \n")
    bid = int(input("What is your bid? \n"))
    bidders.update({name:bid})
    other_bidders = input("Are there more bidders? Type 'yes' or 'no': \n")
    if other_bidders == "yes":
        print("\n" * 20)
    else:
        break
max_bid = 0
winner = ""
for key in bidders:
    if bidders[key] > max_bid:
        max_bid = bidders[key]
        winner = key
print(f"The winner is {winner} with a bid of ${max_bid}")