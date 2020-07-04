# ## Merge Sort

# In[46]:


count = 0


def merge_sorted(L):
    global count
    count += 1
    if len(L) < 2:
        return L
    else:
        mid = len(L) // 2
        left = merge_sorted(L[:mid])
        right = merge_sorted(L[mid:])  # Depth-first search
        print(f"Recursion Level {count}")
        print(f"Left: {left}, Right: {right}")
        merged = merge2(left, right)
        print(f"Merge Result: {merged}\n")
        return merged


def merge(left, right):
    result = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) == 0:
        result.extend(right)
    else:
        result.extend(left)
    return result


def merge2(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


Lst = [8, 4, 1, 6, 5, 9, 2, 0]
Lst = merge_sorted(Lst)
Lst