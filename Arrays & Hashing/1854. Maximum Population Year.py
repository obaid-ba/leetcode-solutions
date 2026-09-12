def maximumPopulation(logs):
    maxi = 0
    res =0
    for year in range(1950,2051):
        population = 0
        for person in logs:
            birth = person[0]
            death = person[1]
            if birth <= year <death:
                population +=1
        if population > maxi:
            maxi = population
            res = year
    return res