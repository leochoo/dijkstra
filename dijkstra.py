# edited July 10th 2018 to show the shortest path and also get rid of the unncessary code

from collections import defaultdict
import math

class Graph():
    def __init__(self):
        self.nodes = []
        self.edges = defaultdict(int)

    def add_edge(self, node1, node2, distance):
        self.edges[(node1, node2)] = distance
        self.edges[(node2, node1)] = distance

class Node():
    def __init__(self, name):
        self.name = name
        #shortest distance from start node
        self.shortest_dist = math.inf
        self.prev = None

#calculate distance between two nodes
def dist(graph, startNode, endNode):
    # Warning: I passed in the node type above but USE node.NAME below!
    result = graph.edges[(startNode.name, endNode.name)]
    if result != 0:
        #return if directly connected
        return result
    else:
        #if no direct connection, return shortest path to it
        shortest_path = findShortestPath(startNode, endNode)
        return shortest_path

def dijkstra(graph, startName, destName):
    startNode = None
    destNode = None
    visited = [] # this might not be necessary at the end so I might be able to remove this
    unvisited = []

    for node_str in graph.nodes: #graph.nodes = ['A', 'B', 'C', 'D', 'E']
        #create node objects
        newNode = Node(node_str)
        #add to the list of unvisited nodes
        unvisited.append(newNode)
        #assign values tostartNode and destNode
        if node_str == startName:
            # A is 0 apart from A
            startNode = newNode
            startNode.shortest_dist = 0
        if node_str == destName:
            destNode = newNode

    while unvisited:
        #choose unvisited node with the smallest known shortest_dist
        #first make list of shortest distance from unvisited
        unv_dist = []
        for n in unvisited:
            unv_dist.append(n.shortest_dist)
        min_dist = min(unv_dist)
        for node in unvisited:
            if node.shortest_dist == min_dist:
                currNode = node
        for node in unvisited:
            # if non-zero edge exists from currNode to target,
            if graph.edges[(currNode.name, node.name)] != 0:
                #then it is a neighborNode
                neighborNode = node
                temp_dist = dist(graph, startNode, currNode) + dist(graph, currNode, neighborNode)
                if temp_dist < neighborNode.shortest_dist:
                    neighborNode.shortest_dist = temp_dist
                    neighborNode.prev = currNode
        #remove from unvisited node
        unvisited.remove(currNode)
        #push to visited node
        visited.append(currNode)

    return findShortestPath(startNode, destNode)

def findShortestPath(startNode, destNode):
    global trails
    #caculate shortest path by adding all prev values
    shortestPath = 0
    temp_vertices = [] #showPath
    while destNode != startNode:
        shortestPath += dist(graph, destNode, destNode.prev)
        temp_vertices.append(destNode.name)
        destNode = destNode.prev
    temp_vertices.append(destNode.name)
    trails = list(temp_vertices) #showPath
    return shortestPath

def showPath():
    global trails
    trails = list(reversed(trails)) #reverse to show in the order from start -> dest
    for i in trails:
        if i == trails[-1]:
            print(i)
        else:
            print(i, end="->")

if __name__ == '__main__':
    trails = []
    graph = Graph()
    nodes = ['A', 'B', 'C', 'D', 'E']
    for node in nodes:
        graph.nodes.append(node)

    graph.add_edge('A', 'B', 6)
    graph.add_edge('A', 'D', 1)
    graph.add_edge('D', 'B', 2)
    graph.add_edge('D', 'E', 1)
    graph.add_edge('B', 'E', 2)
    graph.add_edge('B', 'C', 5)
    graph.add_edge('C', 'E', 5)

    print(dijkstra(graph, 'A', 'C')) # output: 7
    showPath()
    print(dijkstra(graph, 'A', 'E')) # output: 2
    showPath()
    print(dijkstra(graph, 'A', 'B')) # output: 3
    showPath()
    print(dijkstra(graph, 'D', 'C')) # output: 6
    showPath()
    print(dijkstra(graph, 'A', 'A')) # output: 0
    showPath()
