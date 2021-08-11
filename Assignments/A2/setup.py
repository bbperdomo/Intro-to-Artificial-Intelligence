import numpy as np, random, operator
import pandas as pd



#------------------------------------------
# Classes
#----------------------------------------

#Creates and handles cities
#A city is comprised of an x and y coordinate
class City:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    #calculates distance b/w 2 cities using pythogorean theorem
    def distance(self,city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance
    
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"



#Calculates fitness
#Fitness is the inverse of the route distance
#Since the goal is to minimize route distance, a larger
#fitness score is better
class Fitness:
    def __init__(self,route):
        #a list of 25 cities from list of 100 cities is passed in
        self.route = route
        self.distance = 0
        self.fitness = 0.0

    #stores/returns
    def routeDistance(self):
        if self.distance == 0:
            pathDistance = 0
            #print(len(self.route))
            #loops through each xy pair of a given list in population
            for i in range(0, len(self.route)):
                #marks 1st xy pair as fromCity
                #Ex: (34,76)
                fromCity = self.route[i]
                toCity = None

                #calculating if start and end at the same city
                if i + 1 < len(self.route):
                    #sets the toCity for current fromCity, sets connection
                    toCity = self.route[i + 1]
                else:
                    #makes the toCity of the last xy pair the 1st xypair
                    #connects last city to 1st
                    toCity = self.route[0]
                    #tuples(xy pairs) are City objs which can use distance()
                    #fromCity is calling distance to calc dist from toCity
                    #distance() returns dist b/w current city and next city, and adds it to path distance
                pathDistance += fromCity.distance(toCity)
            #for loop ends up summing ALL distances b/w every xy pair(city)
            self.distance = pathDistance
        return self.distance

    def routeFitness(self):
        if self.fitness == 0:
            #routeDistance() returns the total summed up distance
            #for all cities in a given list(individual)

            ##path_distance is inversed and stored as score for this particular route
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness


#------------------------------------------
# Creating initial population
#----------------------------------------

#route generator
#Creating an individual involves randomly selecting
#the order in which cities are visited
#Produces 1 individual
def createRoute(cityList):

    #sample() is an inbuilt function of the random module
    #returns a list of len(cityList) number of unique elements sampled randomly
    route = random.sample(cityList, len(cityList))
    #route is a list (randomized list of city xy pairs)
    return route

#Creates an entire population of routes
#We've created 100 individuals that now make up a population
def initialPopulation(popSize, cityList):
    #population is a list of lists containing city coords(xy pairs), which are the many possible routes
    #it contains 100 lists of xy coord tuples
    population = []

    #loop executes 100 times since popSize is 100
    for i in range(0, popSize):
        
        population.append(createRoute(cityList))
    return population

    