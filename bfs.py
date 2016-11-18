
__author__ = 'Aarushi'

def parse_input(input):
	mydic = {}
	temp = input.split(' ')
	for temp1 in temp:
		s = temp1.split('->')
		if s[0] not in mydic:
			mydic[s[0]] = []
		mydic.get(s[0]).append(s[1])

	return mydic

def bfs(graph, start_node=None):
	bfs = []
	
	if start_node == None:
		start_node = graph.keys()[0]
	if start_node not in graph:
		raise Exception('invalid start node given')
	queue =[start_node]
	parents_graph = {start_node:None}
	while len(queue) != 0:
		node = queue.pop(0)
		if node not in bfs:
			bfs.append(node)
			for values in graph.get(node,[]):
				if values not in parents_graph:
					parents_graph[values] = node
			queue.extend(graph.get(node,[]))
	return parents_graph

input = raw_input('Enter the connections of the graph in the format a->b seperated by space:')
graph = parse_input(input)
print bfs(graph)
