record_in_sec = float(input())
distance = float(input())
time_per_meter = float(input())

delay = distance // 50 * 30
attempt = distance * time_per_meter + delay

diff = abs(attempt - record_in_sec)

if attempt < record_in_sec:
    print(f'Yes! The new record is {attempt:.2f} seconds.')
else:
    print(f'No! He was {diff:.2f} seconds slower.')
