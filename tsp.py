#!/usr/bin/env

'''
# CS325 Project 4 - Traveling Salesman Problem
# Ava Cordero
# Alston Godbolt
# Soo-Min Yoo
    Starting from a degenerate tour consisting of the two farthest 
cities, repeatedly choose the non-tour city with the minimum 
distance to its nearest neighbor among the tour cities, and make 
that city the next in the tour.
'''
import sys,numpy
from math import *
from collections import OrderedDict
# from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

# Function Get_Distance returns the distance of two tuples a=(x1,y1),b=(x2,y2)
def get_distance(a,b):
    # return square root of ( (x2-x1)^2 + (y2-y1)^2 )
    return sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

# Greedy approximation tour construction algorithm
# Add nodes to graph whose distance to the last tour node is minimal
def greedy_construction (graph):
    # Step 1. Find two cities farthest from each other to create a starting tour.

    # initialize an ordered dict of cities
    tour_coords = OrderedDict()
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
            distance = get_distance(a,b)

            # if the calculated distance is greater than the current max distance, update the max distance
            if distance > max_distance:
                max_distance = distance
                # update the keys of cities with the maximum inter-city distance
                tour_a = i; tour_b = j

    # the maximum distance is the total distance
    total_distance = max_distance
    # add the cities to the dict of cities
    tour_coords[tour_a] = graph[tour_a]; tour_coords[tour_b] = graph[tour_b]
    # remove the two cities from the graph
    del graph[tour_a]; del graph[tour_b]

    # # compute convex hull using SciPy.spatial
    # hull = ConvexHull(graph.values())
    # # # add the cities to the dict of cities
    # tour_coords = OrderedDict()
    # for vertex in hull.vertices:
    #     # add the vertex to tour_coords
    #     tour_coords[vertex] = hull.points[vertex] 
    #     # remove the vertex from the graph
    #     del graph[vertex]
    
    # Step 2. Repeatedly add a city from the graph with the maximum distance from the last city added to the tour, until graph is empty.
    
    # while there are cities left in graph,
    while len(graph) > 0:
        # initialize a second ordered dict for containing a city to later put into the tour
        city = OrderedDict()
        # initialize min distance
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
        # add the nearest city to the city dict
        city[tour_city] = tour_coord   
        # add nearest city to the tour
        tour_coords.update(city)
        # ------------------------------------                        

        # remove the city from the graph
        if len(graph) is not 0:
            del graph[tour_city]

    # add to the total distance the distance from the last node back to the first node.
    total_distance += get_distance(tour_coords[next(iter(tour_coords))],
    	tour_coords[next(reversed(tour_coords))])

    # write the total distance and new line individually -- experienced some bug
    output.write(str(int(total_distance)))
    output.write('\n')

    return tour_coords

# Function 2-OPT(route, i, k):
# Takes a tour and spit out something better.
def two_opt (graph):
    # initialize new_route
    new_route = []

    # # 1. take route[1] to route[i-1] and add them in order to new_route
    # while true:
    #     min_chage = 0
    #     for i in range(0, graph-2):
    #         for j in range(i+2, graph):
    #             change = get_distance(i, j) + get_distance(i+1,j+1) - get_distance(i,i+1) - get_distance(j,j+1)
    #             if(min_change > change):
    #                 min_change = change
    #                 mini_i = i
    #                 mini_j = j
    #                 break

    # 2. take route[i] to route[k] and add them in reverse order to new_route
    #while true:
 #       best_dist = calc_Total(existing_route) <-- can we calc the delta instead? that will be O(n)
 #       for i in range(0, cities):
 #           for j in range(i+1, cities):
 #               new_route = (two_opt, i, k)
 #               new_dist = calc_Total(new_route)
 #               if(new_dist < best_dist):
 #                   existing_route = new_route
 #                   break

    # 3. take route[k+1] to end and add them in order to new_route

    # return new_route;
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
        graph[int(node)] = [float(x),float(y)]
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
    # validate the input and assign it to graph
    graph = validate(sys.argv)
    # find the best tour we can
    tour = tsp(graph)
    # print out each city index
    for key,value in tour.iteritems():
        # write the key and new line individually -- experienced some bug
        output.write(str(key))
        output.write('\n')

    # Test-code to plot the tour
    # Assign tour keys for plotting.
    pts = numpy.array(tour.values())
    # print pts
    # Get the indices of the hull points.
    hull_indices = numpy.array(tour.keys())
    # print hull_indices
    # These are the actual points.
    hull_pts = pts[hull_indices,:]

    plt.plot(pts[:, 0], pts[:, 1], 'ko', markersize=3)
    plt.fill(hull_pts[:,0], hull_pts[:,1], fill=False, edgecolor='b')
    # plt.xlim(0, x)
    # plt.ylim(0, y)
    plt.show()
    # #

    return


if __name__ == '__main__':
    output = open(sys.argv[1]+'.tour','w+')
    main()
    exit()
