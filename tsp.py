#!/usr/bin/env

'''
# CS325 Project 4 - Traveling Salesman Problem
# Ava Cordero
# Alston Godbolt
# Soo-Min Yoo
    Starting from a degenerate tour consisting of the two closest 
cities, repeatedly choose the non-tour city with the minimum 
distance to its nearest neighbor among the tour cities, and insert 
it in between the two consecutive tour cities for which such an 
insertion causes the minimum increase in total tour length.
'''

import sys
from math import *
from collections import OrderedDict

# Function greturns the distance of two tuples a=(x1,y1),b=(x2,y2)
def get_distance(a,b):
    return sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

# Greedy approximation tour construction algorithm
# Add nodes to graph whose distance to the last tour node is minimal
def greedy_construction (graph):
    # Step 1. Find two cities farthest from each other to create a starting tour.

    # initialize an ordered dict of cities
    cities = OrderedDict()
    # initialize max distance
    max_distance = 0
    # initialize total distance traveled
    total_distance = 0
    # initialize keys of cities to remove from graph
    tour_a = 0; tour_b = 0

    # while there are cities left to be checked,
    for i in range(0, len(graph)-1): # loop a
        for j in range(i+1, len(graph)): # loop b
            # pick next two cities in graph to check inter-city distance
            a = graph[i]; b = graph[j]
            # get distance between first city a and a second city b
            # square root of ( (x2-x1)^2 + (y2-y1)^2 )
            distance = get_distance(a,b)

            # if the calculated distance is greater than the current max distance, update the max distance
            if distance > max_distance:
                max_distance = distance
                # update the keys of cities with the maximum inter-city distance
                tour_a = i; tour_b = j

    # add the cities to the dict of cities
    cities[tour_a] = graph[tour_a]; cities[tour_b] = graph[tour_b]
    # remove the two cities from the graph
    del graph[tour_a]; del graph[tour_b]
    # turn dict of cities into the new starting tour
    tour_coords = OrderedDict(cities.items())
    
    # Step 2. Repeatedly add a city from the graph with the maximum distance from the last city added to the tour, until graph is empty.
    
    # while there are cities left in graph,
    while len(graph) > 0:
        # initialize a second ordered dict for containing a city to later put into the tour
        city = OrderedDict()
        # reset max distance
        min_distance = float('inf')
        # initialize key of city to remove from graph
        tour_city = 0
        # for each city in graph,
        for key,value in graph.iteritems():
            # set city a as the latest city added to the tour and set city b as the next city to check in graph
            c = tour_coords[next(reversed(tour_coords))]; 
            d = value        
            # get distance between city a and city b
            distance = get_distance(c,d)

            # if the calculated distance is less than the current min distance, update the max distance and key of that farthest city
            if distance < min_distance:
                min_distance = distance
                # update the key of city with the min inter-city distance to latest city in tour
                tour_city = key
                tour_coord = value

        # keep a running sum of the total distance traveled
        total_distance += min_distance
    
        # ------------------------------------
        # add farthest city to the city dict
        city[tour_city] = tour_coord   
        # add farthest city to the tour
        tour_coords.update(city)
        # ------------------------------------                        

        # remove the city from the graph
        if len(graph) is not 0:
            del graph[tour_city]
    total_distance += get_distance(tour_coords[next(iter(tour_coords))],
    	tour_coords[next(reversed(tour_coords))])
    output.write(str(total_distance)+'\n')
    return tour_coords


# 2-OPT - Take a tour and spit out something (hopefully!) better.
def two_opt (graph):
    # Add 2-OPT code
    return graph

# TSP - Combine farthest insertion and 2-opt.
def tsp (graph):
    return two_opt(greedy_construction(graph))

#Converts txt file to python dict of format {node:(x,y)}
def file_to_dict (file):
    graph = {}
    file = open(file,'r+')
    for line in file:
        (node,x,y) = line.split()
        graph[int(node)] = (int(x),int(y))
    return graph

# Validates input file and calls file_to_dict() to return a valid
def validate (arg_list=[],*arg):
    # Add validation code
    if len(arg_list) is 2:
        arg = arg_list[1]
        if arg.lower().endswith('.txt'):
            try:
                graph = file_to_dict(arg)
            except:
                print "Input file line format must be 'N X Y' for Node number, X-coordinate, and Y-coordinate."
                exit()
            return graph
        else:
            print "Accepts .txt files exclusively."
            exit()
    else:
        print "Accepts 1 argument input file exclusively."
        exit()

# Main function
def main ():
    graph = validate(sys.argv)
    output = open('./output.txt','w+')
    tour = tsp(graph)
    for key,value in tour.iteritems():
    	output.write(str(key)+'\n')
    return


if __name__ == '__main__':
    output = open('./output.txt','w+')
    main()
    exit()
