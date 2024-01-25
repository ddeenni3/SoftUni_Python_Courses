import re


pattern = r'([|#])([A-Za-z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d+)(\1)'

string = input()

matches = re.findall(pattern, string)

total_cal = 0

for match in matches:
    total_cal += int(match[5])

print(f'You have food to last you for: {total_cal // 2000} days!')

for match in matches:
    item = match[1]
    expiration_date = match[3]
    calories = match[5]
    print(f"Item: {item}, Best before: {expiration_date}, Nutrition: {calories}")
