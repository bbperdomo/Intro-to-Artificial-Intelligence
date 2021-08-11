from setup import *

#-----------------------------
#Determining Fitness
#-----------------------------
 #Fitness defines how well a solution performs. 

def rankRoutes(population):
    #init dictionary
    fitnessResults = {}
    #loop executes 1oo times since len(pop) = 100 (100 list objects)
    for i in range(0, len(population)):
        #iterate through the 100 lists of cities(routes), compute the fitness score + store in dict
        fitnessResults[i] = Fitness(population[i]).routeFitness()
        #return the keys(city x-y coords) in descending order as a new list
        #itemgetter(1) dictates list is sorted by 2nd index
    #print(fitnessResults)
    return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)

#----------------------------
#Parent Selection
#----------------------------

#Roulette Wheel Selection
#Every individual has a chance to be selected, but those with better fitness scores have a larger chance of being selected
#Calculates a relative fitness weight
#popRanked is a 100 item dict w/ index mapped to fitness scores
def selection(popRanked, eliteSize):
    selectionResults = []
    #a dataframe is a 2D data structure comprised of labeled axis rows/columns
    #df is the instatiation of our pandas dataframe, and takes
    #a numpy array as its data arg
    df = pd.DataFrame(np.array(popRanked), columns=["Index","Fitness"])

    #this creates a new column in the data frame displaying all fitness scores summed cumulatively
    df['cum_sum'] = df.Fitness.cumsum()
    #similar to above, creates a new column displaying cumulative percentage
    df['cum_perc'] = 100*df.cum_sum / df.Fitness.sum()
    #print(df)

    #Concept of elitism is used here, to ensure the fittest live on
    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i][0])
    for i in range(0, len(popRanked) - eliteSize):
        pick = 100*random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i,3]:
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults

#----------------------------
#Mating pool
#----------------------------

#Extracts the individuals we determined to be most fit from selection()
def matingPool(population, selectionResults):
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])
    return matingpool

#----------------------------
#Crossover Strategies
#---------------------------- 

#Ordered crossover - to account for including all cities exactly one time
def breed(parent1,parent2):
    child = []
    childP1 = []
    childP2 = []

    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent2))

    startGene = min(geneA, geneB)
    endGene = max(geneA,geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])

    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 +childP2
    return child

def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0,eliteSize):
        children.append(matingpool[i])

    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool)-i-1])
        children.append(child)
    return children


#----------------------------
#Mutation Strategies
#---------------------------- 

#Swap mutation

def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if(random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))

            city1 = individual[swapped]
            city2 = individual[swapWith]

            individual[swapped] = city2
            individual[swapWith] = city1
    return individual


#Extended mutate function for entire population
def mutatePopulation(population, mutationRate):
    mutatedPop = []

    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop


#----------------------------
#Next Generation
#---------------------------- 
#produces a new generation
#First routes are ranked, then parents are selected via selection(),
#The mating pool is then created via matingPool()
#new gen is created using breedPopulation, and then mutated


def nextGeneration(currentGen, eliteSize, mutationRate):
    popRanked = rankRoutes(currentGen)
    selectionResults = selection(popRanked,eliteSize)
    matingpool = matingPool(currentGen, selectionResults)
    children = breedPopulation(matingpool, eliteSize)
    nextGeneration = mutatePopulation(children, mutationRate)
    return nextGeneration

#----------------------------
#Genetic Algorithm
#---------------------------- 
#

def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations):
    #popSize = 100, population is list of 25 cities
    #pop contains a list of 100 lists containing 25 xy pairs a piece
    pop = initialPopulation(popSize, population)
    #print(pop)
    
    #initial distance. 1/ b/c distance is inverse of fitness
    #[0][1] accesses 1st index of pop dict which is the 1st route
    #then accesses 2nd index of
    #dividing 1 by the fitness score gives us the init distance
    print("initial distance: " + str(1 / rankRoutes(pop)[0][1]))
    #print(str(rankRoutes(pop)[0][1]))
    
    for i in range(0,generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)
        

    print("Final distance: " + str(1 / rankRoutes(pop)[0][1]))
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute