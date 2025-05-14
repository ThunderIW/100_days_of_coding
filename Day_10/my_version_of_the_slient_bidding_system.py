bidders={}
bids=[]
print("""

                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
""")
while True:
    bidders_name=str(input("What is your name?:"))
    bidders_bid=int(input("What is your bid?: $"))

    bidders[bidders_name]=bidders_bid

    print(bidders)

    bidders_remaining=input("Are there any other bidders? Type 'yes or no'. ")
    if bidders_remaining.lower()=='no':
        break

    else:
        continue

for bidders_id,name in enumerate(bidders):
    amount_bid=bidders[name]
    bids.append(amount_bid)

winner_name=max(bidders,key=bidders.get)
print(f"The winner is {winner_name} with a bid of ${bidders[winner_name]}.")





