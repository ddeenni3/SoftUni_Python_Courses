from math import floor

record_time_in_seconds = float(input())
distance_in_meters = float(input())
swimming_distance_per_second_in_meters = float(input())

record_attempt_time = distance_in_meters * swimming_distance_per_second_in_meters

delay = floor(distance_in_meters / 15) * 12.5

record_attempt_time += delay

diff = abs(record_attempt_time - record_time_in_seconds)

if record_attempt_time < record_time_in_seconds:
    print(f'Yes, he succeeded! The new world record is {record_attempt_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {diff:.2f} seconds slower.')

