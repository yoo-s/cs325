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
# Insert the node whose minimal distance to a tour node is maximal. The idea behind this 
# strategy is to fix the overall layout of the tour early in the insertion process.
def farthest_insertion (graph):	
	# The starting tour is usually some tour on three nodes, e.g. those nodes that form the largest triangle. 
	# For Euclidean problems, a good starting tour is the tour that follows the convex hull of all nodes.  
	# Step 1. Start with a sub-graph consisting of the largest triangle convex hull.
	
	# How to choose next node to be inserted.
	# A new node is inserted into the tour at the point that causes the minimum increase in the length 
	# of the tour.
	# Step 2. Find node r such that cir is maximal and form sub-tour i-r-i.
	
	# Where to insert chosen node.
	# Step 3. (Selection step) Given a sub-tour, find node r not in the sub-tour farthest from any node in the sub-tour; i.e. with maximal crj
	
	# Step 4. (Insertion step) Find the arc (i, j) in the sub-tour which minimizes cir + crj - cij . Insert r between i and j.
	
	# Step 5. If all the nodes are added to the tour, stop. Else go to step 3
	
	return graph

# 2-OPT tour improvement algorithm
def two_opt (graph):
	# 
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
		(node,x,y) = line.split()
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
