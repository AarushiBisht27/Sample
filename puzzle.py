
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
	queue =[(start_node, None)]
	parents_graph = {}
	while len(queue) != 0:
		node, parent = queue.pop(0)
		if node not in bfs:
			parents_graph[node] = parent
			bfs.append(node)
			childs = [(i, node) for i in graph.get(node,[])]
			queue.extend(childs)
	return parents_graph
def dfs(graph, start_node=None):
	dfs = []
	if start_node == None:
		start_node = graph.keys()[0]
	if start_node not in graph:
		raise Exception('invalid start node given')
	stack =[(start_node, None)]
	parents_graph = {}
	while len(stack) != 0:
		node, parent = stack.pop()
		if node not in dfs:
			parents_graph[node] = parent
			dfs.append(node)
			childs = [(i, node) for i in graph.get(node,[])]
			stack.extend(childs)
	return parents_graph		
def take_input():
	puzzle = []
	start_pos = None
	end_pos = None
	row = 0
	while True:
		user_input = raw_input().strip()
		if user_input=='':
			break
		end = user_input.find('$')
		if end != -1:
			end_pos = ( row, end )
		start = user_input.find('s')
		if start != -1:
			start_pos = ( row, start )
		puzzle.append(list(user_input))
		row += 1
	return (start_pos, end_pos, puzzle)
	
def parse_puzzle(puzzle):
	graph = {}
	for y,row in enumerate(puzzle):
		for x,row_element in enumerate(row):
			if row_element != '#':
				if (y,x) not in graph:
					graph[(y,x)] = []
				for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
					if 0 <= x+i < len(row) and 0 <= y+j < len(puzzle):
						if puzzle[y+j][x+i] != '#':
							graph[(y,x)].append((y+j,x+i))

	return graph
def print_output(puzzle, parents, start_pos, end_pos):
	p = parents.get(end_pos)
	if not p:
		print "path not found!"
		return
	while p:
		if p != start_pos:
			y,x = p
			puzzle[y][x] = '*'
		p = parents[p]
	for i in puzzle:
		print ''.join(i)
input = raw_input("Choose bfs or dfs algorithm to solve the puzzle:\n")
parents=[]
start_pos, end_pos, puzzle = take_input()
graph = parse_puzzle(puzzle)
if(input == "bfs"):
	parents = bfs(graph, start_pos)
elif(input == "dfs"):
	parents = dfs(graph, start_pos)
else:
	print "Option not valid!"

print_output(puzzle, parents,start_pos, end_pos)
