def price_calculator(product: str, n: int) -> float:
    if product == 'coffee':
        return n * 1.50
    elif product == 'water':
        return n * 1.00
    elif product == 'coke':
        return n * 1.40
    elif product == 'snacks':
        return n * 2.00


product_type = input()
quantity = int(input())

total_price = price_calculator(product_type, quantity)

print(f'{total_price:.2f}')
