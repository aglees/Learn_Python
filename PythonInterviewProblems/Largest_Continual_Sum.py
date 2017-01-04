def large_cont_sum(arr): 
    
    summation = 0
    on_streak = False
    on_streak_start_sum = 0
    max_summation = 0
    
    for i in range(len(arr)):
                  
        if summation < (summation + arr[i]):
            # sum would increase addition of  new item
            # new potentially winning streak, or continuation
            if not on_streak:
                on_streak = True
                on_streak_start_sum = summation
                max_summation = summation + arr[i]
            else:
                max_summation = summation + arr[i]
            
            summation += arr[i]
                                  
        if summation > (summation + arr[i]):
            # new sum would be less than existing sum
            # not the end, but we need to be careful
            if on_streak:
                if summation + arr[i] < on_streak_start_sum:
                    #end of streak
                    #reset sum for streak
                    on_streak = False
                    on_streak_start_sum = (summation + arr[i])
                    summation = 0
                else:
                    # not below starting streak some, so do nothing
                    if max_summation < (summation + arr[i]):
                        max_summation = summation
                    summation += arr[i]
            else:
                # not on a streak, and sum less than starting point, so reset summation to zero.
                summation = 0
                
    return max_summation

def large_cont_sum_answer(arr):
    
    # Check to see if array is length 0
    if len(arr) == 0:
        return 0
    
    max_sum = current_sum =  arr[0]
    
    for num in arr[1:]:    
        current_sum = max(current_sum+num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum

lst = [-1,1]
lst = [1,2,-1,3,4,10,10,-10,-1]
print (large_cont_sum_answer(lst))
