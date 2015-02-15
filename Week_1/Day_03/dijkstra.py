# Dijkstra's Algorithm 

# CURRENT STATUS: Works on Wikipedia example

class Graph:       
    def __init__(self, number_of_nodes=0):        
        self.nodelist = []
        self.edgedict = {} 
        if number_of_nodes > 0:            
            n = 1
            while n <= number_of_nodes:
                Node(self)                
                n += 1     
        elif number_of_nodes != 0:
            print "number of nodes should be nonnegative integer!"            
    
    def size(self):
        return len(self.nodelist)     
    
    def createnode(self):
        Node(self)
        
    def createedge(self, node1, node2, weight):
        Edge(self, node1, node2, weight)    
        
    def ingraph(self, node):
        return node in self.nodelist      

    def node_number(self, number):
        # print number
        return self.nodelist[number] 

    def edge(self, node1, node2):
        return self.edgedict[(node1, node2)]    

class Node:
    def __init__(self, graph):         
        self.graph = graph
        graph.nodelist.append(self)
        self.index = graph.nodelist.index(self)
        
    def adjacent_nodes(self):         
        return {
        node for node in self.graph.nodelist if (self,
        node) in self.graph.edgedict
        }        
    
    # def connect(self, othernode, weight=None):
        # if othernode in self.graph:           
            # edge = Edge(self, othernode, weight)
            # graph.edgelist.append(edge)
        # else:
            # print "othernode not in same graph!"       
        
        
class Edge:
    def __init__(self, graph, node1, node2, weight=None):
        if node1 and node2 in graph.nodelist:
            self.nodes = (node1, node2) # or {node1, node2}? graph directed? 
            self.weight = weight
            graph.edgedict[self.nodes] = self
            if weight >= 10**90:
                print "Warning: Dijkstra implementation assumes 10**100 = infinity!"
        else:
            print "Nodes must be in graph!"
        
    def coincides(self, edge):
        return self.nodes == edge.nodes 


def dijkstra(graph, origin_index):
    origin = graph.node_number(origin_index)
    nodes = graph.nodelist
    N = graph.size()
    D = []
    for node in nodes:
        D.append(10**100) # "infinity"    
    marked_nodes = set()
    D[origin_index] = 0
    a = origin_index        
    while marked_nodes != set(nodes):
        # print a
        # print [node.index for node in marked_nodes]
        # print [node.index for node in set(nodes)]        
        # print graph.node_number(a).adjacent_nodes()       
        distance_a = {
        node:graph.edge(
        graph.node_number(a), node
        ).weight for node in graph.node_number(a).adjacent_nodes()
        }
        # print distance_a        
        V = {
        node for node in nodes if (
        node in graph.node_number(a).adjacent_nodes()
        ) and (not (node in marked_nodes))
        }
        # print V
        for node in V:
            # print D[node.index]
            D[node.index] = min([D[node.index], D[a] + distance_a[node]])
            # print D[node.index]
        marked_nodes.add(graph.node_number(a))  
        if marked_nodes != set(nodes):  
            # print [i for i in range(len(D)) if not nodes[i] in marked_nodes]
            E = [
            D[i] for i in range(len(D)) if not nodes[i] in marked_nodes
            ]
            F = {
            i:D[i] for i in range(len(D)) if not nodes[i] in marked_nodes
            }            
            for i in F:
                if D[i] == min(E):
                    a = i
                    break
        # print D        
    return D   
    
print "Welcome to a Python implementation of Dijkstra's algorithm!"   

N = input("Enter the number of nodes in your graph\n")
graph = Graph(N)

for index in range(N): 

    input = raw_input(
    "Enter the nodes adjacent to (i.e. that can be reached directly from)\
    Node {number}, separated only by commas. \
    (If none, enter {number}.) \n".format(number = index+1)
    )
    adjacent_node_indices = [int(n) - 1 for n in input.split(',')]
    for n in adjacent_node_indices:
        weight = int(
        raw_input(
        "Enter the distance from Node {first} to Node {second}.\
        (If same, enter 0.) \n".format(first = index+1, second = n+1))
        )
        graph.createedge(
        graph.node_number(index), graph.node_number(n), weight
        )
        # print graph.node_number(index).adjacent_nodes
        
        
origin_index = int(raw_input("Enter the starting node. \n")) - 1

results = dijkstra(graph, origin_index)

for i in range(len(results)):
    print "The distance from Node {origin} to Node {destination}\
    is {result}".format(
    origin = origin_index +1, destination = i+1, result = results[i]
    )


        
        
    


        
    
    