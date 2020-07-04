#!/usr/bin/env python
# coding: utf-8

# # MIT 6.00.2X Unit 1
# 
# ## Lessons Learned
# 
# - 0/1 knapsack problem and fractional knapsack problem/ optimization problem
# - Maximizing or minimizing the objective function while satisfying the constraints
# - Greedy algorithm and locally optimal solution
# - Power set, decision tree (or search tree) for enumerating all possible combinations
# - Brute force algorithm, globally optimal solution and its exponential complexity
# - Dynamic programming, memoization; optimal substructure and repeating subproblems
# - Graphs, digraphs, nodes and edges
# - Modelling a graph problem
# - Shortest path algorithm
# 
# 
# ## Coding Practice
# 
# - Write a generalized greedy algorithm
# - Write a program for getting power set of a given set both iteratively and recursively
# - Write a program on brute force algorithm
# - Use dynamic programming for getting the power set recursively and use it in brute force algorithm
# - Write a program on building graphs; creating classes for graphs, digraphs, nodes and edges
# - Write a program on shortest path and minimum time for graphs

# ## 0/1 Knapsack Problem

# ### Generalized Greedy Algorithm

# In[45]:


class item(object):
    def __init__(self, name, value, weight):
        self.name = name
        self.weight = weight
        self.value = value
    def getName(self):
        return self.name
    def getWeight(self):
        return self.weight
    def getValue(self):
        return self.value
    def getValForWeight(self):
        return self.value/self.weight
    def howLight(self):
        return 1/self.getWeight()
    def __repr__(self):
        return "{0.name}: ({0.weight}, {0.value})".format(self)
    
def buildItems(filename):
    file = open(filename,'r')
    item_lst = file.readlines() #Returns a list of list of lines in the file
    item_lst = [item.rstrip() for item in item_lst] #Removing carriage return
    item_obj = [] #List of items as objects
    for x in item_lst:
        x = x.split(',')
        item_obj.append(item(x[0], int(x[1]), int(x[2]))) #Object creation
    return item_obj

def testGreedy(item_obj, maximum_weight):
    print("Use greedy by value for weight to allocate", maximum_weight, 'kg')
    greedy(item_obj, item.getValForWeight, maximum_weight)
    print("\nUse greedy by less heavy to allocate", maximum_weight, 'kg')
    greedy(item_obj, item.howLight, maximum_weight)
    print("\nUse greedy by value to allocate", maximum_weight, 'kg')
    greedy(item_obj, item.getValue, maximum_weight)

def greedy(item, objFunction, constraint):
    item = sorted(item, key = objFunction, reverse = True)
    total_weight, total_value = 0, 0
    item_taken = []
    for x in item:
        if x.getWeight() + total_weight <= constraint:
            item_taken.append(x)
            total_weight += x.getWeight()
            total_value += x.getValue()
    return printGreedy(item_taken, total_value)

def printGreedy(item_taken, total_value):
    print(f"Total value of the items taken = {total_value}")
    for item in item_taken:
        print("\t", item)

filename = r"C:\Users\G KARTHIK RAJA\Desktop\Backup\MOOCs\Introduction_to_Computational_Thinking_and_Data_Science\Burglar items.txt"
item_obj = buildItems(filename)
maximum_weight = 20
testGreedy(item_obj, maximum_weight)


# #### Lessons Learned
# - How to customize the sorting of list of objects using keyFunction
# - How to create a list of objects using the data from a text file
