def check_ticket(some_ticket):
    if len(some_ticket) != 20:
        return 'invalid ticket'
    symbols = ['@', '#', '$', '^']
    left_side = some_ticket[:10]
    right_side = some_ticket[10:]
    for symbol in symbols:
        for uninterrupted_symbol_length in range(10, 5, -1):
            winning_symbol = symbol * uninterrupted_symbol_length
            if winning_symbol in left_side and winning_symbol in right_side:
                if uninterrupted_symbol_length == 10:
                    return f'ticket "{some_ticket}" - {uninterrupted_symbol_length}{symbol} Jackpot!'
                return f'ticket "{some_ticket}" - {uninterrupted_symbol_length}{symbol}'
    return f'ticket "{some_ticket}" - no match'


tickets = [x.strip() for x in input().split(', ')]

for ticket in tickets:
    print(check_ticket(ticket))
