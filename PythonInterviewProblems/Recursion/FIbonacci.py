def fib_recursion(n):

    if n <= 1:
        
        return n

    return fib_recursion(n-1) + fib_recursion(n-2)

def fib_dynamic(n, results=None):

    if not results:  
        results = { 0:0, 1:1 }
    
    while n not in results:
        fib_1 = fib_dynamic(n-1, results)
        fib_2 = fib_dynamic(n-2, results)
        fib =  fib_1 + fib_2
        results[n] = fib
        
    return results[n]

# print(fib_recursion(10))
print(fib_dynamic(100))
# 0 1 1 2 3 5