deposited_amount = float(input())
deposit_time_months = int(input())
interest_rate = float(input())
interest_rate /= 100  # converting interest rate to percentage

total_amount = deposited_amount + deposit_time_months * ((deposited_amount * interest_rate) / 12)

print(total_amount)
