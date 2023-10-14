def wealth_distributor(population: list, minimum_wealth: int):
    for current_person_wealth in range(len(population)):
        wealthiest = population.index(max(population))
        if population[current_person_wealth] < minimum_wealth:
            if population[wealthiest] - (minimum_wealth - population[current_person_wealth]) < minimum_wealth:
                return 'No equal distribution possible'
            population[wealthiest] -= minimum_wealth - population[current_person_wealth]
            population[current_person_wealth] += minimum_wealth - population[current_person_wealth]
    return population


some_population = [int(x) for x in input().split(', ')]
current_minimum_wealth = int(input())

print(wealth_distributor(some_population, current_minimum_wealth))
