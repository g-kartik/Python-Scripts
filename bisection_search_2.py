# ## Bisection Search 2

# In[8]:


def bisect_search2(L, e):
    def bisect_search2_helper(L, e, low_index, high_index):
        if low_index == high_index:
            if L[low_index] == e:
                return (True, low_index)
            else:
                return (False, None)
        else:
            mid_index = (low_index + high_index) // 2
            mid_val = L[mid_index]
            if mid_val == e:
                return (True, mid_index)
            elif mid_val > e:
                return bisect_search2_helper(L, e, low_index, mid_index - 1)
            else:
                return bisect_search2_helper(L, e, mid_index + 1, high_index)

    if len(L) == 0:
        return (False, None)
    else:
        return bisect_search2_helper(L, e, 0, len(L) - 1)


foo = [0, 1, 2, 3, 5, 9]
ele = 5

(isFound, index) = bisect_search2(foo, ele)

if isFound:
    print(f"{ele} is found at index {index}")
else:
    print(f"{ele} is not found")