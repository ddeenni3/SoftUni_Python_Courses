agency_name = input()
adult_tickets = int(input())
kid_tickets = int(input())
adult_ticket_price = float(input())
service_fee = float(input())


kid_ticket_price = adult_ticket_price * 0.3
kid_ticket_price += service_fee


total_cost = (kid_tickets * kid_ticket_price) + (adult_tickets * (adult_ticket_price + service_fee))

profit = total_cost * 0.2

print(f'The profit of your agency from {agency_name} tickets is {profit:.2f} lv.')
