#!/usr/bin/env python
# coding: utf-8

# ## Brute Force Algorithm

# In[33]:


class item(object):
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def getValForWeight(self):
        return self.value/self.weight
    def howLight(self):
        return(1/self.weight)
    def __repr__(self):
        return "{0.name}:({0.value}, {0.weight})".format(self)

def buildItem(filename):
    file = open(filename, 'r')
    item_list = file.readlines()
    item_list = [item.rstrip() for item in item_list]
    item_obj = []
    for i in item_list:
        i = i.split(',')
        item_obj.append(item(i[0], int(i[1]), int(i[2])))
    return item_obj

def brute(toConsider, avail, memo = {}):
    brute.count += 1
    if toConsider == [] or avail == 0:
        return (0,())
    elif toConsider[0].getWeight() > avail:
        return brute(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        key = (len(toConsider), avail)
        if key in memo:
            return memo.get(key)
        else:
            withVal, withToTake = brute(toConsider[1:], avail - nextItem.getWeight())
            withVal += nextItem.getValue()
            withoutVal, withoutToTake = brute(toConsider[1:], avail)
            if withVal > withoutVal:
                result = (withVal, withToTake + (nextItem,))
                memo[key] = result
                return result
            else:
                result = (withoutVal, withoutToTake)
                memo[key] = result
                return result
            
def printBrute(result):
    print(f"Total value of the items taken is {result[0]}")
    print(f"\nTotal number of times function 'Brute' was called = {brute.count}")
    for item in result[1]:
        print('\t', item)

def testBrute(item_obj, maximum_weight):
    print("\nUse brute force by value to allocate", maximum_weight, 'kg')
    printBrute(brute(item_obj, maximum_weight))
                        
filename = r"C:\Users\G KARTHIK RAJA\Desktop\Backup\MOOCs\Introduction_to_Computational_Thinking_and_Data_Science\Burglar items.txt"
item_obj = buildItem(filename)
maximum_weight = 200
brute.count = 0
testBrute(item_obj, maximum_weight)           





