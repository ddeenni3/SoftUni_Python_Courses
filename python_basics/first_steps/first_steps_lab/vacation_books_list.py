amount_of_pages = int(input())
pages_per_hour = int(input())
days_for_reading = int(input())

total_time_for_book = amount_of_pages / pages_per_hour

hours_per_day = total_time_for_book / days_for_reading

print(int(hours_per_day))
