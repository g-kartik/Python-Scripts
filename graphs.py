#!/usr/bin/env python
# coding: utf-8

# ## Class - Node

# In[36]:


class node(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def __repr__(self):
        return self.name


# ## Class - Edge

# In[37]:


class edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __repr__(self):
        return "{0.src} -> {0.dest}".format(self)


# ## Class - Digraph

# In[4]:


class digraph(object):
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if node.getName() in self.edges:
            raise ValueError('Duplicate Node')
        else:
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Nodes are not present to add the edge')
        else:
            self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        else:
            raise NameError(name)
    def hasNode(self, node):
        return node in self.edges
    def __repr__(self):
        result = ""
        for src in self.edges:
            for dest in self.edges[src]:
                result += src.getName() + ' -> ' + dest.getName() + '\n'
        return result[:-1]


# ## Class - Graph

# In[5]:


class graph(digraph):
    def addEdge(self, edge):
        digraph.addEdge(self, edge)
        rev = edge(edge.getDestination(), edge.getSource())
        digraph.addEdge(self, rev)


# ## Build - Graph

# In[6]:


def buildGraph(graphType, file1, file2):
    g = graphType()
    file1 = open(file1)
    node_list = file1.readlines()
    node_list = [n.rstrip() for n in node_list]
    for n in node_list:
        g.addNode(node(n))
    file2 = open(file2)
    edge_list = file2.readlines()
    edge_list = [e.rstrip() for e in edge_list]
    for e in edge_list:
        e = e.split(',')
        src, dest = g.getNode(e[0]), g.getNode(e[1])
        g.addEdge(edge(src,dest))
    return g

file1 = r"C:\Users\G KARTHIK RAJA\Desktop\Backup\MOOCs\Introduction_to_Computational_Thinking_and_Data_Science\Nodes.txt"
file2 = r"C:\Users\G KARTHIK RAJA\Desktop\Backup\MOOCs\Introduction_to_Computational_Thinking_and_Data_Science\Edges.txt"
g = buildGraph(digraph, file1, file2)


# ## Depth First Search Algorithm

# In[7]:


def DFS(graph, start, end, path, shortest):
    path += [start]
# This if statement is responsible for stopping the depth wise search by avoding further 
# recursive calls when destination node is reached
    if start == end:
        return path
    else:
# This for loop serves two purposes:
# 1. Depth Wise: It first traverses the first children node of every node due to recursive calls
# 2. Breadth Wise: If any node do not have any children node or we hit the destination node 
# then that node is not explored depth wise because any further recursive calls will be avoided 
# so the for loop backtracks to the previous DFS node call and continues with the depth wise 
# exploration of the next children node. So by exploring the next children node, the loop has 
# started breadth wise exploration. Since the loop executes first depth wise and then breadth 
# wise, therefore it is called as Depth First Search
        for node in graph.childrenOf(start):
# This if statement is also responsible for stopping the depth wise search by avoiding further
# recursive calls when node is already visited
            if node not in path:
# This if statement is also responsible for stopping the depth wise search by avoiding further
# recursive calls when the path containing this node is larger than the shortest path. Also, it
# does the same thing when path retuned by previous DFS call is equal to the shortest path and
# that happens when this node has no children nodes.
                if shortest == None or len(path) < len(shortest):
                    new_path = DFS(graph, node, end, path, shortest)
# This if statement checks whether previous if statement was true and new_path is not None, i.e.
# whether this node has children nodes and returned a shorter path
                if new_path != None:
                    shortest = new_path
    return shortest

def shortestPath(graph, start, end, toPrint):
    start, end = graph.getNode(start), graph.getNode(end)
    shortest = DFS(graph, start, end, [], None)
    return shortest
        
print(shortestPath(g, 'Boston', 'Phoenix', True))


# In[8]:


def DFS(graph, start, end, path, shortest, toPrint = False):
    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                new_path = DFS(graph, node, end, path, shortest, toPrint)
            if new_path != None:
                shortest = new_path
        elif toPrint:
            print('Already visited', node)
    return shortest

def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result

def shortestPath(graph, start, end, toPrint = False):
    start, end = graph.getNode(start), graph.getNode(end)
    shortest = DFS(graph, start, end, [], None, toPrint)
    if shortest != None:
        print(f"The shortest path from {start} to {end} is:\n{printPath(shortest)}")
    else:
        print(f"There is no path from {start} to {end}")
    pass

shortestPath(g, 'Boston', 'Phoenix', True)  


# ## Breadth first search using recursion

# In this algorithm we evaluate all the children nodes of the start node in a breadth wise iterative fashion to check for the following things:
# - Whether it is the destination node, if true then shortest path solution is obtained.
# - Whether it has been already visited, if false then the program stores the node and its path as a start node for the next recursive call, else it is skipped.

# In[32]:


def BFS(graph, startNodesLst, end, toPrint = False):
    newStartNodes = []
    for nodeData in startNodesLst: #nodeData is a tuple having node and its path
        for node in graph.childrenOf(nodeData[0]):
            path = nodeData[1]
            if node == end:
                if toPrint:
                    print(printPath(path + [node]))
                return path + [node]
            elif node not in path: #storing node and its path as a tuple
                if toPrint:
                    print(printPath(path + [node]))
                newStartNodes.append((node, path + [node])) 
    if len(newStartNodes) != 0:
        shortest_path = BFS(graph, newStartNodes, end, toPrint)
        if shortest_path != None:
            return shortest_path
    else:
        return None

def testBFS(graph, start, end, toPrint = False):
    start, end = graph.getNode(start), graph.getNode(end)
    startNodesLst = [(start,[start])]
    result = BFS(graph, startNodesLst, end, toPrint)
    if result != None:
        print(f"The shortest path from {start} to {end} is:\n{printPath(result)}")
    else:
        print(f"No path found from {start} to {end}")
        
def printPath(path):
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result
              
testBFS(g, "Boston", "Phoenix", True)
#testBFS(g, "Los Angeles", "Phoenix")


# ## Breadth first search using iteration

# In[35]:


def BFS(graph, start, end, toPrint = False):
    newStartNodes = [(start,[start])]
    while len(newStartNodes) != 0:
        startNodesLst = newStartNodes.copy()
        newStartNodes.clear()
        for nodeData in startNodesLst: #nodeData is a tuple having node and its path
            for node in graph.childrenOf(nodeData[0]):
                path = nodeData[1]
                if node == end:
                    if toPrint:
                        print(printPath(path+[node]))
                    return path + [node]
                elif node not in path: #storing node and its path as a tuple
                    if toPrint:
                        print(printPath(path + [node])) 
                    newStartNodes.append((node, path + [node]))
    return None

def testBFS(graph, start, end, toPrint = False):
    start, end = graph.getNode(start), graph.getNode(end)
    result = BFS(graph, start, end, toPrint)
    if result != None:
        print(f"The shortest path from {start} to {end} is:\n{printPath(result)}")
    else:
        print(f"No path found from {start} to {end}")
        
def printPath(path):
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result
              
testBFS(g, "Boston", "Phoenix", True)
#testBFS(g, "Los Angeles", "Phoenix", True)


# In[26]:





# In[ ]:




