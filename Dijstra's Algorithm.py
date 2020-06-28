from graphviz import *
import os
os.environ["PATH"] += os.pathsep + './venv/Lib/site-packages/graphviz/release/bin'

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

#Creating a dictionary for effective storage of the graph

def graph():
    vertices = []
    x = int(input('Enter the number of vertices/Nodes in your Graph :'))
    for i in range(x):
        v = input('Enter the vertex no.{}  :'.format(i+1))
        vertices.append(v)
    print(vertices)
    graph = {}
    while True:
        v = input('Enter the source node (vertex) :')
        if (v not in vertices):
            print('Input node is not a part of the graph.')
            continue
        if(v in graph):
            print('The vertex {} has already been updated.'.format(v))
            continue
        else:
            print('For the node {}'.format(v))
            adjacent = {}
            while True:
                s = input('Enter the destination vertex :')
                try:
                    wt = int(input(f'Enter the Cost between {v} and {s} :'))
                except ValueError:
                        print('Enter an integer value')
                        wt = int(input('Enter the cost between {v} and {s} :'))
                if (s in adjacent):
                    print('The edge exists already')
                    break
                elif(s not in vertices):
                    print(f'The node {s} is not a part of the graph')
                    continue
                adjacent[s] = wt
                print(adjacent)
                quitt = input(f"Type 'y' to stop updating the Node {v} or press Enter").upper()
                if (quitt == 'Y'):
                    break
            graph[v] = adjacent
        st = input("Type 'y' to stop updating the edges or press Enter:").upper()
        if (st == 'Y'):
            break
    return graph

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================


'''Shortest path algorithm '''

def dijkstra(graph,source,destination):

    least_cost = {}                     #to store the cost of reaching every node, constantly updated
    predecessor = {}                    #keeps track of the predecessors while travelling from source to destination node
    unseenNodes = graph                 #to iterate through all nodes
    infinity = 999999                  #infinity-a very large value
    path = []                           #to record the path as we reach the destination 

    # Initially the shortest distance to reach all the nodes is assumed to be infinity

    for node in unseenNodes:
        least_cost[node] = infinity

    least_cost[source] = 0
    #the cost to reach the source node from itself is zero


    # Loop to traverse all nodes in graph

    # while traversing the graph, we determine the min_distance_node every time.


    while unseenNodes:
        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node

            elif least_cost[node] < least_cost[min_distance_node]:
                min_distance_node = node

    # determining all possible paths from the min_dist_node

        possible_paths = graph[min_distance_node].items()

    # calculating the "cost"  for each path we take and updating if it is lower than the existing cost

        for neighbor, weight in possible_paths:

            if weight + least_cost[min_distance_node] < least_cost[neighbor]:

                least_cost[neighbor] = weight + least_cost[min_distance_node]

                predecessor[neighbor] = min_distance_node

    # Removing the nodes that were already visited

        unseenNodes.pop(min_distance_node)

     #When destination node is reached, the path is traced back till the source node
     #Calculating the total cost

    currentNode = destination

    while currentNode != source:

        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,source)


    #  If final cost is infinity, the node couldn't be reached or its too far away

    if least_cost[destination] != infinity:
        print(f'Shortest distance between {source} and {destination} is :' + str(least_cost[destination]))
        print('And the path traced is :')
        print(*path,sep=" → ")
        print("CAUTION ! Close the PDF file to run the program again")
    else :
        print("Node is too far away to calculate its shortest path or couldn't be reached")

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

'''Function for creating visualisation of graph'''

def visual_graph(input_graph):
    g = Graph(filename='Graph', engine='sfdp')
    edgelist = []
    for i in input_graph:
        g.node(i)
        for j in input_graph[i]:
            n = (i, j)
            m = (j, i)
            edgelist.append(n)
            if n and m not in edgelist:
                g.edge(i, j, label=str(input_graph[i][j]))
    return g.view()

##############################################################################################################################################################
##############################################################################################################################################################
##############################################################################################################################################################
##############################################################################################################################################################


########          TESTING           #################

p = {
                'a':{'b':8,'c':2, 'd':3},
                'b':{'c':4,'f':5,'a':8},
                'c':{'f':16,'d':4,'a':2,'b':4},
                'd':{'a':3,'c':4,'e':9, 'g':1},
                'e':{'g':5, 'h':6,'d':9,'f':7},
                'f':{'e':7, 'h':8,'b':5,'c':16},
                'g':{'h':1,'e':5,'d':1},
                'h':{'g':1,'e':6,'f':7}
    }


n = input(f"This is current graph:\n {p},\n "
          f"Type 'Update' if you want if you want to input a new graph or "
          f"press ENTER to continue with this graph:").upper()

if n == "UPDATE":
    input_graph = graph()
    print(input_graph)
    visual_graph(input_graph)
else :
    input_graph = p
    print(input_graph)
    visual_graph(input_graph)


#________________________________________________________________________________________________________________________________________________________________


cond = False
while cond is False:
    starting_node = input("Enter starting node for Shortest path present in INPUT GRAPH :").strip()
    destination_node = input("Enter destination node present in INPUT GRAPH :").strip()
    if(starting_node in input_graph and destination_node in input_graph):
        cond = True
        dijkstra(input_graph,starting_node,destination_node)
        while 1:                   #infinite loop to keep the execution window open
            pass
    else:
        print('The entered nodes are not a part of the input graph')
    continue
        
