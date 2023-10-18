price_without_tax = 0
tax = 0

is_special = False
while True:
    command = input()
    if command == 'special' or command == 'regular':
        if command == 'special':
            is_special = True
        break
    current_price = float(command)
    if current_price < 0:
        print('Invalid price!')
        continue
    price_without_tax += current_price
    tax += current_price * 0.2

total_price = price_without_tax + tax
if is_special:
    total_price *= 0.9

if total_price == 0:
    print('Invalid order!')
else:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {price_without_tax:.2f}$\n"
          f"Taxes: {tax:.2f}$\n"
          f"-----------\n"
          f"Total price: {total_price:.2f}$"
          )
