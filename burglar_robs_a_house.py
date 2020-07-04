#!/usr/bin/env python
# coding: utf-8

# # Burglar Robs a House
# As a burgler robs a house, she finds the following items:
# 
#     Dirt - Weight: 4, Value: 0
#     Computer - Weight: 10, Value: 30
#     Fork - Weight: 5, Value: 1
#     Problem Set - Weight: 0, Value: -10
# 
# This time, she can only carry a weight of 14, and wishes to maximize the value to weight ratio of the things she
# carries. She employs three different metrics in an attempt to do this, and writes an algorithm in Python to
# determine which loot to take.
# 
# The algorithm works as follows:
# 
# Evaluate the metric of each item. Each metric returns a numerical value for each item.
# For each item, from highest metric value to lowest, add the item if there is room in the bag.

# In[47]:


'''Class definition for items'''
class Items(object):
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        
    def getWeight(self):
        return self.weight
    
    def getValue(self):
        return self.value
    
    def density(self):
        return self.value/ self.weight
    
    def __str__(self):
        return self.name + ': <' + str(self.weight) + ', ' + str(self.value) + '>'   


# In[48]:


'''Raw Data'''
names = ["Dirt", "Computer", "Fork", "Problem_Set"]
weights = [4, 10 ,5 ,0]
values = [0, 30 , 1, -10]
maxWeight = 14
keyFunction = Items.getValue #Objective Function


# In[49]:


'''Object Creation'''
def buildItems(names, weights, values):
    items = []
    for i in range(len(values)):
        items.append(Items(names[i], weights[i], values[i]))
    return items

items = buildItems(names, weights, values)


# In[50]:


def greedy(items, maxWeight, keyFunction):
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    totalWeight, totalVal = 0, 0
    taken = []
    for i in range(len(itemsCopy)):
        if totalWeight + itemsCopy[i].getWeight() <= maxWeight:
            taken.append(str(itemsCopy[i]))
            totalWeight += itemsCopy[i].getWeight()
            totalVal += itemsCopy[i].getValue()
    return (taken, totalVal)    


# In[51]:


greedy(items, maxWeight, keyFunction)


# The above solution is not optimal as the 'Problem_Set' reduced the total value by 10

# In[54]:


def greedy2(items, maxWeight, keyFunction):
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    totalWeight, totalVal = 0, 0
    taken = []
    for i in range(len(itemsCopy)):
        if totalWeight + itemsCopy[i].getWeight() <= maxWeight         and itemsCopy[i].getValue() >= 0:
            taken.append(str(itemsCopy[i]))
            totalWeight += itemsCopy[i].getWeight()
            totalVal += itemsCopy[i].getValue()
    return (taken, totalVal) 


# In[55]:


greedy2(items, maxWeight, keyFunction)


# This is the optimal solution

# In[ ]:




