budget = float(input())
ticket_type = input()
amount_of_people = int(input())

transport_cost = 0
ticket_price = 0

if 1 <= amount_of_people <= 4:
    transport_cost += budget * 0.75
elif 5 <= amount_of_people <= 9:
    transport_cost += budget * 0.6
elif 10 <= amount_of_people <= 24:
    transport_cost += budget * 0.5
elif 25 <= amount_of_people <= 49:
    transport_cost += budget * 0.4
else:
    transport_cost += budget * 0.25

if ticket_type == 'VIP':
    ticket_price += amount_of_people * 499.99
elif ticket_type == 'Normal':
    ticket_price += amount_of_people * 249.99

total_sum = transport_cost + ticket_price
diff = abs(budget - total_sum)

if budget >= total_sum:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')
