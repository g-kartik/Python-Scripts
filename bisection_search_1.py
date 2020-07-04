# ## Bisection Search 1

# In[48]:


def bisect_search1(L, e):
    """
    Input: L, sorted list to be seached in; e, element to be searched for.
    Return: (True, index) if found else (False, None).
    Declarative Statement: If middle element value is equal to e, return True, else  e in the list
    reduced by half each
    """
    if len(L) == 0:
        return False

    elif len(L) == 1:
        return L[0] == e

    else:
        mid_index = len(L) // 2
        mid_val = L[mid_index]

        if mid_val > e:
            return bisect_search1(L[:mid_index], e)
        else:
            return bisect_search1(L[mid_index:], e)


foo = [0, 1, 2, 3, 5, 9]
ele = 9

isFound = bisect_search1(foo, ele)
if isFound:
    print(f"{ele} is found")
else:
    print(f"{ele} is not found")