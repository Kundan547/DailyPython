graph = {
  'S' : ['A','B', 'C'],
  'A' : ['D'],
  'B' : ['E'],
  'C' : ['F', 'J'],
  'D' : ['G'],
  'E' : ['I', 'J'],
  'F' : ['S'],
  'J' : [],
  'G' : ['H'],
  'I' : [],
  'J' : [],
  'H' : ['D']
}

visited = []
queue = []   

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue: 
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("Following is the Breadth-First Search")
bfs(visited, graph, 'S')    # function calling
