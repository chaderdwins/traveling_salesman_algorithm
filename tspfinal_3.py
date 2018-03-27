#!/usr/bin/python3
from math import sqrt, pow
import sys, re, math, time, os, copy

def main(input_file):

	tsp = TSP(input_file)
	file_size = os.path.getsize(input_file)
	if file_size < 10000:#10000
		start_time = time.time()
		#a nearest neighbor algorithm that aids in
		#getting a coherent path so optimization is
		#more effective
		cities1 = []
		for key in tsp.cities:
		    cities1.append([key, tsp.cities[key][0], tsp.cities[key][1]])
		distanceLength,optimizedWay = tsp.NN(cities1)
		end_time = time.time()
		total_time = end_time - start_time
		optimizedWay.insert(0, distanceLength)
		del(optimizedWay[-1])
		tsp.output_results(input_file, optimizedWay)
		#print(distanceLength)
		#print(optimizedWay)
	else:
	    start_time = time.time()
	    trip = tsp.build_route()
	    trip = tsp.two_opt(trip)
	    end_time = time.time()
	    total_time = end_time - start_time
	    tsp.output_results(input_file, trip)
	print("Run-time: " + str(total_time), 's')


class TSP:

    #Initialized on start of program by arg[1]
    def __init__(self, input_file):
        self.cities = self.parse_input(input_file)


    def NN(self, cities):
        edge = sys.maxsize
        numberCities = len(cities)
        theWay = []
        for i in range(numberCities):
            notVisited = copy.deepcopy(cities)
            del notVisited[i]
            thePath = []
            thePath.append(cities[i][0])
            distance = 0

            xBefore = cities[i][1]
            yBefore = cities[i][2]

            while notVisited:
                min_distance = sys.maxsize
                futureCity = 0

                for city in notVisited:
                    presentDis = self.determineDistance(xBefore, yBefore, city[1], city[2])
                    if (min_distance > presentDis):
                        min_distance = presentDis
                        futureCity = cities.index(city)

                thePath.append(futureCity)
                notVisited.pop(notVisited.index(cities[futureCity]))
                xBefore = cities[futureCity][1]
                yBefore = cities[futureCity][2]
                distance += min_distance
                if edge < distance:
                    break
            distance += self.determineDistance(xBefore, yBefore, cities[i][1], cities[i][2])
            thePath.append(thePath[0])
            if edge > distance:
                edge = distance
                theWay = copy.deepcopy(thePath)
        return edge, theWay

    def determineDistance(self, xOne, yOne, xTwo, yTwo):
        DistanceD = int(round(sqrt(pow((xOne - xTwo), 2) + pow((yOne - yTwo), 2))))
        return DistanceD


    def two_opt(self, route):
        distance = route[0]
        route = route[1:]
        for i in range(len(self.cities) - 2):
            for j in range(i + 1, len(self.cities) - 1):
                # dist1 is current distance between pair of points, dist2 is the swapped distance
                dist1 = self.distance_between(route[i], route[i + 1]) + self.distance_between(route[j], route[j + 1])
                dist2 = self.distance_between(route[i], route[j]) + self.distance_between(route[i + 1], route[j + 1])
                if dist2 < dist1:
                    new_route = self.two_swap(route, i, j)
                    distance = distance - dist1 + dist2
                    route = new_route
        return [distance] + route

    def two_swap(self, route, x, y):
        return route[:x + 1] + route[y:x:-1] + route[y + 1:]

    #Nearest neighbor algorithm to set up coherent path
    def build_route(self):
        current_city = 0
        route = [current_city]
        unvisited = {x for x in self.cities.keys()} #tracker for unvisited cities
        unvisited.remove(current_city)
        total_d = 0  #total distance

        while (len(unvisited) > 0):
            #choose city with lowest edge weight
            min = 9999999  #minimum distance to nearest city
            for city in unvisited:  #for each city
                distance = self.distance_between(current_city, city)
                if distance < min:
                    min = distance
                    next_city = city

            total_d += min  #update total distance
            current_city = next_city  #move to next city
            route += [current_city]  #add city to tour
            unvisited.remove(current_city)  #mark visited

        #Final leg added
        total_d += self.distance_between(route[0], route[len(route) - 1])
        return [total_d] + route #tour distance is [0], since number of cities varies

    # Get the input data into dict format
    def parse_input(self, in_file):

        file = open(in_file, 'r')
        line = file.readline()

        cities = dict()
        #cities consist of city # as the key and x,y coordinates as the values
        while len(line) > 1:

            line_parse = re.findall(r'[^,;\s]+', line)
            cities[int(line_parse[0])] = [int(line_parse[1]), int(line_parse[2])]
            line = file.readline()

        file.close()

        # return vertices, i.e. cities
        return cities

    # output results with .tour file extension
    def output_results(self, input_file_name, travel_list="No Results Generated"):

        # append .tour to original input file
        filename = input_file_name + ".tour"

        # write each value in travel_list on separate line
        with open(filename, 'w') as f:
            for value in travel_list:
                f.write(str(value) + '\n')
            f.close()

    def distance_between(self, city1, city2):
        cities_x = self.cities.get(city1)[0] - self.cities.get(city2)[0]
        cities_y = self.cities.get(city1)[1] - self.cities.get(city2)[1]
        return int(round(math.sqrt(cities_x * cities_x + cities_y * cities_y)))

if __name__ == '__main__':
    main(sys.argv[1])
