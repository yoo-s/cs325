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
def farthest_insertion (graph):
	return graph

# 2-OPT tour improvement algorithm
def two_opt (graph):
	return graph

# TSP management function
def tsp (graph):
	farthest_insertion(graph)
	two_opt(graph)
	return graph

#Converts txt file to python dict of format {node:(x,y)}
def file_to_dict (file):
	graph = {}
	file = open(file,'r+')
	for line in file:
		(node,x,y) = line.split(" ")
		graph[int(node)] = (x,y)
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
