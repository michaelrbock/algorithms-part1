import sys
import resource
import heapq

# data structures to hold adjacency list
GRAPH = {} # {node: [outgoing_edges]}
NODES = []

# hold the status of wether a node has been visited or not
visited = {} # {node: True/False}

# hold the 'finishing time' of each node
finishing_time = {} # {finishing_time: node}

# hold the 'leader' of each node
leader = {} # {node: leader}

count = 0

# read data into data structures to hold graph
with open('SCC.txt', 'r') as f:
	for data_line in f:
		line = data_line.split()
		if line[0] in GRAPH:
			GRAPH[line[0]].append(line[1])
		else:
			GRAPH[line[0]] = [line[1]]
		if line[0] not in NODES:
			NODES.append(line[0])
		if line[1] not in NODES:
		 	NODES.append(line[1])
		visited[line[0]] = False
		visited[line[1]] = False
		count += 1
		if count % 50000 == 0:
			print count

print "DATA IN,IN DATA STRUCT"

# sort NODES
NODES = [int(x) for x in NODES]
NODES = sorted(NODES)
NODES = [str(x) for x in NODES]

print "READ AND SORTED"

# global variable for finishing times in 1st pass
# holds the # of nodes processed so far
t = 0
# global variable for leaders in 2nd pass
# holds the current source vertext
s = None

def dfs(graph, source):
	global t

	visited[source] = True
	# set leader to most recent source in dfs_loop
	leader[source] = s

	# for each edge (source, arc)
	if source in graph:
		for arc in graph[source]:
			# if arc not yet explored
			if arc in graph:
				if not visited[arc]:
					dfs(graph, arc)
			elif arc not in graph and not visited[arc]:
				visited[arc] = True
				leader[arc] = s
				t += 1
				finishing_time[t] = arc

	t += 1
	finishing_time[t] = source

def dfs_loop(graph, nodes):
	global s
	global t
	for node in nodes:
		if node in graph:
			if not visited[node]:
				s = node
				dfs(graph, node)
		elif node not in graph and not visited[node]:
			visited[node] = True
			leader[node] = node
			t += 1
			finishing_time[t] = node

def reverse_graph(graph):
	result_graph = {}

	for node in graph:
		for edge in graph[node]:
			if edge in result_graph:
				result_graph[edge].append(node)
			else:
				result_graph[edge] = [node]

	return result_graph

# set up and run Kosaraju's two-pass algorithm
# to find strongly connected components (SCCs)

# reverse direction of arcs in graph
reversed_graph = reverse_graph(GRAPH)

print "REVERSED"

# run dfs_loop on reversed_graph to calculate finishing times
dfs_loop(reversed_graph, reversed(NODES))

print "LOOP 1 COMPLETE"

# extract finishing times into a list
times = finishing_time.keys()
# sort and reverse list so it can be traveresed
times = reversed(sorted(times))
# create list of which order nodes (with original names) should be traversed
new_nodes = []
for time in times:
	new_nodes.append(finishing_time[time])

# reset visited and leader
for node in visited:
	visited[node] = False
	if node in leader:
		del leader[node]
# reset s and t
t = 0
s = None

print "STARTING LOOP 2"

# run dfs_loop on original graph to calculate new leaders
dfs_loop(GRAPH, new_nodes)

print "LOOP 2 COMPLETE"

# holds size of sccs
sccs = {} # {leader: size}

# check leader of nodes to find SCCs
# count number of nodes with each leader to find biggest SCCs
for node in leader:
	if leader[node] in sccs:
		sccs[leader[node]] += 1
	else:
		sccs[leader[node]] = 1

for k, v in sccs.iteritems():
	print v
