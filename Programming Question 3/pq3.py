import sys
from copy import deepcopy
import random 

# read in from stdin, run by doing:
# > cat data.tx | python pq3.py
data = sys.stdin.readlines()

# data structures to hold adjacency list
# original data, not to change
NODES = []
EDGES = {} # {node: [outgoing_edges]}
NUM_OF_EDGES = 0 # this number is double because each edge is represented twice

# arrange data into data structures
for data_line in data:
	line = data_line.split()
	node = line.pop(0)
	NODES.append(node)
	EDGES[node] = []
	for edge in line:
		EDGES[node].append(edge)

# count number of edges
for node in EDGES:
	NUM_OF_EDGES += len(EDGES[node])

def find_cut(nodes, edges, num_of_edges):
	random.seed()
	while len(nodes) > 2:
		rand_int = random.randint(0, num_of_edges-1)
		i = 0 # count of which key
		j = 0 # count of spot in list
		keys = edges.keys()
		for k in range(rand_int):
			if j == len(edges[keys[i]]) - 1:
				i += 1
				j = 0
			else:
				j += 1
		edge_to_combine = (keys[i], edges[keys[i]][j]) # key, connection
		# print edge_to_combine

		# add from edge being deleted to new combined
		for edge in edges[edge_to_combine[1]]:
			# add to new combined edge
			if edge != edge_to_combine[0]:
				edges[edge_to_combine[0]].append(edge)
				edges[edge].append(edge_to_combine[0])

		# delete from dictionary
		del edges[edge_to_combine[1]]
		# delete from list
		nodes.remove(edge_to_combine[1])

		# delete all references to old edge and self loops
		for node in edges:
			for edge in edges[node]:
				if edge == edge_to_combine[1]:
					edges[node] = [x for x in edges[node] if x != edge]
				# check for self loops
				if edge == node:
					edges[node] = [x for x in edges[node] if x != edge]

		# update number of edges by counting
		num_of_edges = 0
		for node in edges:
			num_of_edges += len(edges[node])

		# print nodes
		# print edges
		# print num_of_edges
		# print ""

	# return k (crossing of cut)
	return num_of_edges / 2

# find min cut by running many trials and storing the min cut
min_k = find_cut(deepcopy(NODES), deepcopy(EDGES), deepcopy(NUM_OF_EDGES))
for trial in range(len(NODES) * len(NODES)):
	new_k = find_cut(deepcopy(NODES), deepcopy(EDGES), deepcopy(NUM_OF_EDGES))
	if new_k < min_k:
		min_k = new_k
		print "MIN =", min_k
	print trial # keep track of progress

print min_k