def fib(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    else:
        if n in memo:
            return memo.get(n)
        else:
            result = fib(n-1) + fib(n-2)
            memo.update({n: result})
            return result
print(fib(120))