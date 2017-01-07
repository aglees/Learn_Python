def rec_sum(n):

    if n == 0:
        return 0
    else:
        return n + rec_sum(n-1)

def sum_func(n):
    
    if n // 10 == 0:
        return n
    
    else:       
        
        return n%10 + sum_func(n//10)

print(rec_sum(4))
print(sum_func(4321))
