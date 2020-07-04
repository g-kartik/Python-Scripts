# ### Fibonacci

# In[ ]:


def fib(n):
    """
    Input: Integer, n >= 0
    Returns: Fibonacci of n
    Declarative Statement: Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
    """
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


fib(5)