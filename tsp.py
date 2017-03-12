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

# Farthest insertion tour construction algorithm
# Insert nodes whose minimal distance to a tour node is maximal. The idea behind this 
# strategy is to take a graph of cities and spit out a pretty good (not optimal!) tour.
def farthest_insertion (graph):
    # Step 1. Find two cities farthest from each other to create a starting subtour.

    max_distance = 0
    a_iter = 0; b_iter = 1
    a = graph[a_iter]; b = graph[b_iter]
    best_a = a; best_b = b

    # while there are cities left to be checked,
    while True:
        # get distance between first city a and a second city b
        distance1 = sqrt((bx - ax)**2 + (by - ay)**2)
    
        # set b as another city and calculate the distance between the first city and the newly picked city
        b_iter += 1
        distance2 = sqrt((bx - ax)**2 + (by - ay)**2)

        # if the second calculated distance is greater than the first, update the max distance
        if distance2 > distance1:
            max_distance = distance2

    # update the cities with the maximum inter-city distance
    best_a = a; best_b = b


    # Step 2. Repeatedly add a city from the graph with the maximum distance from the last city added to the tour, until graph is empty.


    # return a pretty good (not optimal) tour
    return tour

# 2-OPT - Take a tour and spit out something (hopefully!) better.
def two_opt (tour):
    # Add 2-OPT code
    return better_tour

# TSP - Combine farthest insertion and 2-opt.
def tsp (graph):
    return two_opt(farthest_insertion(graph))

#Converts txt file to python dict of format {node:(x,y)}
def file_to_dict (file):
    graph = {}
    file = open(file,'r+')
    for line in file:
        (node,x,y) = line.split()
        graph[node] = (int(x),int(y))
    return graph

# Validates input file
def validate (file):
    # Add validation code
    return file

# Main function
def main ():
    file = validate(sys.argv[1])
    print tsp(file_to_dict(file))


if __name__ == '__main__':
    main()
