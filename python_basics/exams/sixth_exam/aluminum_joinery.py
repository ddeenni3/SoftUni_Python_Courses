frame_qty = int(input())
frame_type = input()
delivery = input()

price = 0

if frame_qty < 10:
    print('Invalid order')
else:
    if frame_type == '90X130':
        price += 110
        if 30 < frame_qty <= 60:
            price *= 0.95
        elif frame_qty > 60:
            price *= 0.92
    elif frame_type == '100X150':
        price += 140
        if 40 < frame_qty <= 80:
            price *= 0.94
        elif frame_qty > 80:
            price *= 0.90
    elif frame_type == '130X180':
        price += 190
        if 20 < frame_qty <= 50:
            price *= 0.93
        elif frame_qty > 50:
            price *= 0.88
    elif frame_type == '200X300':
        price += 250
        if 25 < frame_qty <= 50:
            price *= 0.91
        elif frame_qty > 50:
            price *= 0.86

    total = price * frame_qty

    if delivery == 'With delivery':
        total += 60

    if frame_qty > 99:
        total *= 0.96

    print(f'{total:.2f} BGN')
