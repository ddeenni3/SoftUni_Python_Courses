yearly_subscription = int(input())
sneakers = 0.6 * yearly_subscription
equip = 0.8 * sneakers
basketball_ball = 0.25 * equip
accessories = 0.20 * basketball_ball

total_costs = yearly_subscription + sneakers + equip + basketball_ball + accessories
print(total_costs)