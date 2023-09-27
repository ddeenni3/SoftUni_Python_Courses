bill = float(input('The bill is:'))
people = int(input('Split between:'))
tip = int(input('Tip percentage:'))
result = bill / people
total = result + result * (tip / 100)
print(f'You have to pay: {total:.2f}$')
