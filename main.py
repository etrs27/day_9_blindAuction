from replit import clear
from art import logo

print(logo)

auction_active = True
all_bids = []
def get_bid(name, bid):
  new_bid = {}
  new_bid["name"] = name
  new_bid["bid"] = bid
  all_bids.append(new_bid)
def highest_bid():
  winning_bid = 0
  winner = {}
  for bids in all_bids:
    if bids["bid"] > winning_bid:
      winning_bid = bids["bid"]
      winner = bids
  print(f"The winner is {winner['name']} with a bid of ${winner['bid']}!")

while auction_active:
  name = str(input("What is your name?\n")).strip().title()
  bid = int(input("How much are you biding?\n$"))
  get_bid(name, bid)
  other_bids = str(input("Are there any other bidders? Yes or No?\n")).lower().strip()
  if other_bids == "no":
    highest_bid()
    auction_active = False
  else:
    clear()