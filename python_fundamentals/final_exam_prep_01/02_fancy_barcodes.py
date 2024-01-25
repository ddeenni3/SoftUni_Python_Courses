import re

number_of_barcodes = int(input())

pattern = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'

for _ in range(number_of_barcodes):
    barcode = input()
    match = re.findall(pattern, barcode)
    if match:
        match = ''.join(match)
        product_number = re.findall(r'\d+', match)
        product_number = ''.join(product_number) if product_number else '00'
        print(f'Product group: {product_number}')
    else:
        print('Invalid barcode')

