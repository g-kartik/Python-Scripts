#!/usr/bin/env python
# coding: utf-8

# ## Brute Force Algorithm

# Greedy algorithm yields only locally optimal solution. To obtain globally optimal solution, we must use brute force
# algorithm. We will use recursion to generate the power set and we will go through all possible combinations,
# discard the ones which doesn't satisfy the constraints and then find the combination which yields maximum value
# for the given objective function.

# In[2]:

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
        return "{0.name}: ({0.value}, {0.weight})".format(self)

def buildItems(filename):
    file = open(filename,'r')
    item_lst = file.readlines() #Returns a list of list of lines in the file
    item_lst = [item.rstrip() for item in item_lst] #Removing carriage return
    item_obj = [] #List of items as objects
    for x in item_lst:
        x = x.split(',')
        item_obj.append(item(x[0], int(x[1]), int(x[2]))) #Object creation
    return item_obj

def testBrute(item_obj, maximum_weight):
    print("Use brute force by value for weight to allocate", maximum_weight, 'kg')
    brute(item_obj, item.getValForWeight, maximum_weight)
    print("\nUse brute force by less heavy to allocate", maximum_weight, 'kg')
    brute(item_obj, item.howLight, maximum_weight)
    print("\nUse brute force by value to allocate", maximum_weight, 'kg')
    brute(item_obj, item.getValue, maximum_weight)

def brute(item_obj, objFunction, constraint):
    brute.count += 1
    combo = genSubset(item_obj)
    valid_combo = []
    for c in combo:
        total_weight = sum([i.getWeight() for i in c])
        if total_weight <= constraint:
            valid_combo.append(c)
    item_taken = max(valid_combo, key = lambda combo: sum([objFunction(i) for i in combo]))
    total_value = sum([i.getValue() for i in item_taken])
    return printBrute(item_taken, total_value)

def genSubset(lst):
    if len(lst) == 0:
        return [[]]
    else:
        subset_WO_last = genSubset(lst[:-1])
        last = [lst[-1]]
        subset_W_last = [x + last for x in subset_WO_last]
        return subset_WO_last + subset_W_last

def printBrute(item_taken, total_value):
    print(f"Total value of the items taken = {total_value}")
    print(f"Total number of times function 'brute' was called = {brute.count}")
    for item in item_taken:
        print("\t", item)

filename = r"C:\Users\G KARTHIK RAJA\Desktop\Backup\MOOCs\Introduction_to_Computational_Thinking_and_Data_Science\Burglar items.txt"
item_obj = buildItems(filename)
maximum_weight = 200
brute.count = 0
testBrute(item_obj, maximum_weight)


# ## Recursive Implementation

# In[7]:


def maxVal(toConsider, avail):
    maxVal.count += 1
    if toConsider == [] or avail == 0:
        return (0, ())
    elif toConsider[0].getWeight() > avail:
        return maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getWeight())
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
    if withVal > withoutVal:
        result = (withVal, withToTake + (nextItem,))
    else:
        result = (withoutVal, withoutToTake)
    return result

def testBrute(item_obj, maximum_weight):
    print("\nUse brute force by value to allocate", maximum_weight, 'kg')
    printmaxVal((maxVal(item_obj, maximum_weight)))
    
def printmaxVal(result):
    print(f"Total value of the items taken = {result[0]}")
    print(f"Total number of times function 'maxVal' was called = {maxVal.count}")
    for item in result[1]:
        print("\t", item)

maxVal.count = 0    
testBrute(item_obj, maximum_weight)


# In[ ]:




