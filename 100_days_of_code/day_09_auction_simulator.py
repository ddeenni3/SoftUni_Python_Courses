bidders = {}
while True:
    name = input('Please enter your name:\n')
    bid = int(input('Please enter your bid:\n'))
    bidders[name] = bid
    result = input('Are there any more bidders?\nY/N: ').lower()
    if result == 'n':
        break
highest_bidder = ''
highest_bid = 0
for bidder in bidders:
    if bidders[bidder] > highest_bid:
        highest_bid = bidders[bidder]
        highest_bidder = bidder

print(f'The winner is {highest_bidder} with a bid of ${highest_bid}.')
