"""
    Top One
        [1, 2, 1, 3, 4, 2] --> [1, 2]

"""

def top_one(arr):
    population = {}
    result = []
    f_val = 0
    for i in arr:
        if i in population:
            population[i] += 1
        else:
            population[i] = 1

    f_val = max(population.values())

    for k in population.keys():
        if population[k] == f_val:
            result.append(k)

    return result, population

print(top_one([1, 2, 1, 4, 2, 2]))
        