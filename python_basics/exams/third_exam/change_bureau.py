bitcoin = int(input())
chinese_yen = float(input())
commission = float(input())

bitcoin_lev = bitcoin * 1168
chinese_yen_usd = chinese_yen * 0.15
chinese_yen_leva = chinese_yen_usd * 1.76

total = bitcoin_lev + chinese_yen_leva

total_eur = total / 1.95

commission_cost = total_eur * commission / 100

total_eur -= commission_cost

print(f'{total_eur:.2f}')




