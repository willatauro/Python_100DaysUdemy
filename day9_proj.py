


 


from turtle import clearscreen


bids={}

bidding_finished = False 

def find_highest_bidder(bidding_record):

    highest_bid = 0
    for key in bidding_record:

        bid_amount =bidding_record[key]

        if bid_amount > highest_bid :
            highest_bid = bid_amount 
            winner  = key
    
    print (f"The winnder is {key} with a bid of {highest_bid}")

while not bidding_finished:
    name = input("enter your name: ")
    price = int(input ("what is your bid"))
    bids[name]=price


    should_continue = input("Are they more bidders? Type 'yes' or 'no'")

    if should_continue =="no":
        bidding_finished = True
        find_highest_bidder(bids)

    elif should_continue =="yes":
        clearscreen()

    



    