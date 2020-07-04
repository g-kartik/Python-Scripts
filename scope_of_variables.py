### Variable scope
# - formal parameter gets bound to the value of actual parameter when function is called
# - new scope/frame/environment is created when a function is invoked
# - scope is mapping of names to objects
# - function scope/frame is removed after it is executed
# - if no return statement is given, the function returns None value

# ### Inside a function, variable defined outside can be accessed but cannot be modified

def foo():
    print(x) # since we have not defined any local variable x so it refers to global x
    pass
x = 4
foo()


# In[ ]:


def foo1():
    x = 5 # local variable x is defined and binded to 5
    print(x) # local variable x is print not global x
    pass
x = 3
foo1()
print(x) # global x is still unmodified


# In[ ]:


def foo2():
    x = x + 1 #We have not defined x as a local variable and nothing is assigned to it
    #so it refers to global x but since it can only be accessd not modified so we get an error
    pass
x = 2
foo2()
print(x)


# In[ ]:


def foo3():
    global x #By explicitly defining x to be a global variable, we have given the function
    # access to modify it
    x = x + 1
    pass
x = 1
foo3()
print(x)


# In[ ]:


def foo4(x): # formal argument x is assigned to the value of actual argument x = 0
    x = x + 1 # since local variable x is already assigned a value, so it can be modified
    print(x)
    pass
x = 0
foo4(x)
print(x)