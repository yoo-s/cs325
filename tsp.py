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
import sys,time,numpy
from math import *
from collections import OrderedDict,deque
# import matplotlib.pyplot as plt

# define a function-set to quick-peak a deque
def qp (dek):
    if dek:
        var = dek.pop()
        dek.append(var)
        return var
    else:
        return False
def qpl (dek):
    if dek:
        var = dek.popleft()
        dek.appendleft(var)
        return var
    else:
        return False

class dict_deque (object):
    def __init__(self):
        self.v = deque()
        self.k = {}
    def mutate(self,tour):
        self.v = deque(tour.values())
        self.k = {}
        for key,value in tour.iteritems():
            self.k[str(value)] = key
    def append (self,item):
        self.v.append(item.keys()[0])
        self.k[str(item.keys()[0])] = item.values()[0]
    def appendleft (self,item):
        self.v.appendleft(item.keys()[0])
        self.k[str(item.keys()[0])] = item.values()[0]
    def pop (self):
        if qp(self.v):
            key = self.v.pop()
            val = self.k[str(key)]
            return {str(key):val}
    def popleft (self):
        if qpl(self.v):
            key = self.v.popleft()
            val = self.k[str(key)]
            return {str(key):val}
    def qp (self):
        if qp(self.v):
            var = self.pop()
            self.append(var)
            return var
        else:
            return False
    def qpl (self):
        if qpl(self.v):
            var = self.popleft()
            self.appendleft(var)
            return var
        else:
            return False

# Function Get_Distance returns the distance of two tuples a=(x1,y1),b=(x2,y2)
def get_distance(a,b):
    if isinstance(a,dict) and isinstance(b,dict):
        if type(a.keys()) is int: a = a.keys()[1]
        a[0],a[1] = [float(i) for i in a.keys()[0].strip('[]').split(',')]
        b[0],b[1] = [float(i) for i in b.keys()[0].strip('[]').split(',')]
    return sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

# Function Get_Line_length returns the length of a line from u to v
def get_line_length (tour):
    seen = []
    distance = 0
    if isinstance(tour,deque):
        while qp(tour):
            cp = tour.pop()
            if len(seen) > 0:
                distance += get_distance(cp,qp(tour))
            seen.append(qp(tour))
        return distance
    elif isinstance(tour,dict_deque):
        op = tour.pop()
        cp =  op
        while tour.qp():
            cp = tour.qp()
            distance += get_distance(cp.keys(),tour.pop().keys())
        return distance
    elif isinstance(tour,OrderedDict):
        for node in tour:
            if len(seen) > 0:
                distance += get_distance(tour[next(reversed(seen))],tour[node])
            seen.append(node)
        return distance

# Greedy approximation tour construction algorithm
# Add nodes to graph whose distance to the last tour node is minimal
def greedy_construction (graph):
    # Step 1. Find two cities farthest from each other to create a starting tour.
    # initialize an ordered dict of cities
    tour_coords = OrderedDict()
    # initialize max distance
    max_distance = 0
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

    # add the cities to the dict of cities
    tour_coords[tour_a] = graph[tour_a]; tour_coords[tour_b] = graph[tour_b]
    # remove the two cities from the graph
    del graph[tour_a]; del graph[tour_b]
    
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

        # add the nearest city to the city dict
        city[tour_city] = tour_coord   
        # add nearest city to the tour
        tour_coords.update(city)
        # remove the city from the graph
        if len(graph) > 0:
            del graph[tour_city]

    return tour_coords

# Function 2-OPT(route, i, k):
# Takes a tour and spit out something better.
def two_opt (tour):
    # # convert tour values to deque -- need only happen first time...
    new_tour = dict_deque()
    new_tour.mutate(tour)
    swpd = 1
    while swpd == 1:
        # make copy of tour coords
        cur_tour = new_tour
        # initialize a new tour
        new_tour = dict_deque()
        # pop the first and last cities from the old tour to the new
        new_tour.append(cur_tour.pop())
        new_tour.appendleft(cur_tour.popleft())
        swpd = 0
        # while there are at least two tour cities left to check
        while cur_tour.qp() or cur_tour.qpl():
            right_dist = get_distance(new_tour.qp(),cur_tour.qp())
            left_dist = get_distance(new_tour.qp(),cur_tour.qpl())
            # if the two paths cross
            if  right_dist < left_dist:
                # swap dest with neighbors dest
                new_tour.append(cur_tour.popleft())
                new_tour.appendleft(cur_tour.pop())
                swpd = 1
            # else leave the tour as it is.
            else:
                new_tour.append(cur_tour.pop())
                new_tour.appendleft(cur_tour.popleft())
        if cur_tour.qp():
            print 'CTQP!'
            new_tour.append(cur_tour.pop())
        elif cur_tour.qpl():
            print 'CTQPL!'
            new_tour.appendleft(cur_tour.pop())
        else:
            print 'neither'
            swpd = 0
            break
    return new_tour

def output_tour (tour,ofile):
    with open(ofile+'.tour','w+') as output:
        print_list = []
        seen = []
        distance = 0
        if isinstance(tour,dict_deque):
            quick_sum = get_distance(tour.qp(),tour.qpl()) 
            tp = tour.pop()
            while tour.qp():
                print_list += [tour.qp().values()[0]]
                distance += get_distance(tp,tour.pop())
                if tour.qp():
                    tp = tour.qp()
        elif isinstance(tour,OrderedDict):
            quick_sum = get_distance(tour[next(iter(tour))],tour[next(reversed(tour))])
            for node in tour:
                print_list.append(node)
                print node
                if len(seen) > 0:
                    distance += get_distance(tour[next(reversed(seen))],tour[node])
                seen.append(node)
        # print the total distance and new line individually -- experienced some bug
        output.write(str(int(distance + quick_sum)))
        output.write('\n')
        for item in print_list:
            output.write(str(item)+'\n')
    return

def plot_graph (tour):
    # Test-code to plot the tour
    # Uncomment line 16 for graph plotting (not supported on flip).
    # Assign tour keys for plotting.
    pts = numpy.array(tour.values())
    # Get the indices of the hull points.
    hull_indices = numpy.array(tour.keys())
    # These are the actual points.
    hull_pts = pts[hull_indices,:]
    # set the graph configurations
    plt.plot(pts[:, 0], pts[:, 1], 'ko', markersize=3)
    plt.fill(hull_pts[:,0], hull_pts[:,1], fill=False, edgecolor='b')
    # plt.xlim(0, x)
    # plt.ylim(0, y)
    plt.show()
    return

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
                return file_to_dict(arg)
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

    # find the best tour we can and print the runtime.
    t0 = time.clock()
    tour = two_opt(greedy_construction(graph))
    # tour = greedy_construction(graph)
    print 'RUNTIME: ',(time.clock()-t0)

    # output tour data to .tour file
    output_tour(tour,sys.argv[1])
    # plot_graph(tour)
    return

if __name__ == '__main__':
    main()
    exit()
