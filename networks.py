# -*- coding: utf-8 -*-

import numpy as np

class Node():
    """
    Node class. The parameter passed when instantianting is the initial output.
    """
    
    inputs = []
    
    def __init__(self, out):
        self.output = out
        
    def update(self):
        """
        Defines a rule to update the output (from the inputs the node receives)
        This particular rule changes the output to the mean of the inputs.
        """
        
        suma = 0
        for i in self.inputs:
            suma += i
        
        average = suma / float(len(self.inputs))
        
        self.output = np.ceil(average)
        


class Network():
    """
    Creates a network of the list of nodes passed as "nodes", with a list of connections
    for each node. Therefore it is a directed network. connections has to be a list of lists
    for the connections of each node in nodes.
    """
    
    def __init__(self, nodes, connections):
        
        self.nodes = nodes
        self.connections = connections
        
    def assemble(self):
        
        for i in range(len(self.nodes)):
            self.nodes[i].inputs = [ self.nodes[j].output for j in self.connections[i] ] 
            
    def update_nodes(self):
        """
        Calls the update method of each node, so there can be different types of nodes in the network.
        """
        for n in self.nodes:
            n.update()
    
    
    def print_network_state(self):
        
        for i in range(len(self.nodes)):
            
            print "Node {}:".format(i)
            print "output = {}".format(self.nodes[i].output)
            print "inputs = {}\n".format(self.nodes[i].inputs)


## Example in notebook


#a = Node(1)
#b = Node(0)
#c = Node(1)

#conections = [[2,1], [0], [0,2]]
#nodes = [a,b,c]

#net = Network(nodes, connections)

#net.assemble()

#net.print_network_state()


#net.update_nodes()


#net.print_network_state()



