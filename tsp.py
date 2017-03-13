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

    # initialize an empty tour
    tour = {}
    # initialize max distance
    max_distance = 0

    print graph[0]

    # while there are cities left to be checked,
    for i in range(0, len(graph)-1): # loop a
        for j in range(i+1, len(graph)): # loop b
            # pick next two cities in graph to check inter-city distance
            a = graph[i]; b = graph[j]

            # get distance between first city a and a second city b
            distance = sqrt((bx - ax)**2 + (by - ay)**2)
   
            # if the calculated distance is greater than the current max distance, update the max distance
            if distance > max_distance:
                max_distance = distance
                # update the cities with the maximum inter-city distance
                farthest_pair = (a, b)
    # remove the two cities from the graph
    graph.pop(a); graph.pop(b)
    # add the cities to the new subtour
    tour.append(a); tour.append(b)


    # Step 2. Repeatedly add a city from the graph with the maximum distance from the last city added to the tour, until graph is empty.

    # reset max distance
    max_distance = 0

    # while there are cities left in graph,
    while len(graph) > 0:
        # for each city in graph,
        for i in range(0, len(graph)):
            # set city a as the last city added to the tour and set city b as the next city in graph
            a = tour[-1]; b = graph[i]

            # get distance between city a and city b
            distance = sqrt((bx - ax)**2 + (by - ay)**2)
   
            # if the calculated distance is greater than the current max distance, update the max distance and farthest city
            if distance > max_distance:
                max_distance = distance
                farthest_city = b

        
        # remove the farthest city from the graph
        graph.pop(farthest_city)
        # add the city to the new subtour
        tour.append(farthest_city)

    # return a pretty good (not optimal) tour
    return tour


# 2-OPT - Take a tour and spit out something (hopefully!) better.
def two_opt (graph):
    # Add 2-OPT code
    return graph

# TSP - Combine farthest insertion and 2-opt.
def tsp (graph):
    return two_opt(farthest_insertion(graph))

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
    print graph
    # tsp(graph)
    return


if __name__ == '__main__':
    main()
    exit()
