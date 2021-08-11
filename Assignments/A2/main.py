from setup import *
from genetic_algo import *

###########################################################################
###          CAP 4630 - Introduction to Artificial Intelligence  ###
###                                Bryan Perdomo 
###          Assignment 2: Solving TSP with GA's - 7/16/2021    ###
###########################################################################


cityList = []

#creates a list of 25 random x,y coordinate pairs - a random list of cities
for i in range(0,25):
    cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))
#print(cityList)

#Running genetic Algorithm
geneticAlgorithm(population=cityList, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)
