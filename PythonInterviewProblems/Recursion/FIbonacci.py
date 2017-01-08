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
        fib = fib_1 + fib_2
        results[n] = fib
        
    return results[n]

def fib_dynamic2(n, results=None):

    if not results:
        results = {0:0, 1:1}

    while n not in results:
        fib = fib_dynamic2(n-1, results) + fib_dynamic2(n-2, results)
        results[n] = fib

    return results[n]

def fib_iter(n):
    
    series = [0,1]

    if n <= 1:
        return n

    for i in range(2,n+1):

        sum = series[i-1] + series[i-2]

        series.append(sum)

    return sum

def fib_iter2(n):

    series = [0, 1]

    for i in range(2, n+1):

        series.append(series[i-1] + series[i-2])

    return series[n]

def fib_iter3(n):

    a, b = 0, 1

    for i in range(n):

        a, b = b, b + a

    return a

# print(fib_recursion(10))
# print(fib_dynamic(30))
# print(fib_dynamic2(30))
print(fib_iter3(10))
