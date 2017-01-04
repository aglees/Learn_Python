def mergeSort(this_list):
    '''
    Merge sort a list
    '''
    
    if len(this_list) > 1:
        
        mid = len(this_list)//2
        
        lefthalf = this_list[:mid]
        righthalf = this_list[mid:]

        left = mergeSort(lefthalf)
        right = mergeSort(righthalf)

        i=0
        j=0

        output = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                output.append(left[i])
                i=i+1
            else:
                output.append(right[j])
                j=j+1
        output += left[i:]
        output += right[j:]

        return output
    else:
        return this_list


alist = [54,26,93,17,77,31,44,55,20]

print(mergeSort(alist))

#print(mergeSort(alist))
