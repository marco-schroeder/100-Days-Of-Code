import os


def blind_auction():
    logo = '''
                             ___________
                             \         /
                              )_______(
                              |"""""""|_.-._,.---------.,_.-._
                              |       | | |               | | ''-.
                              |       |_| |_             _| |_..-'
                              |_______| '-' `'---------'` '-'
                              )"""""""(
                             /_________\\
                           .-------------.
                          /_______________\\
    '''
    print(logo)
    print("Welcome to the secret auction program!\n")
    auction_dict = {}
    auction_ended = False
    while not auction_ended:
        name = input("What is your name?\n")
        bid = ""
        while not bid.isnumeric():
            bid = input("What is your bid?\n")
        bid = int(bid)
        auction_dict[name] = bid
        other_bidder = ""
        while other_bidder != "yes" and other_bidder != "no":
            other_bidder = input("Are there any other bidders? Type \"yes\" or \"no\".\n").lower()
        if other_bidder == "no":
            auction_ended = True
        if other_bidder == "yes":
            os.system("clear")

    auction_winner_name = max(auction_dict, key=auction_dict.get)
    auction_winner_bid = auction_dict[auction_winner_name]

    print(f"{auction_winner_name} won the secret auction with a bid of ${auction_winner_bid}.")


if __name__ == "__main__":
    blind_auction()
