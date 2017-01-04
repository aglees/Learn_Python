import random

def gen_sample_list(size=10,maxval=10):
    '''
    Generate shuffled, random sample list of size 'n'
    '''
    sample_list = [random.randint(0,maxval) for x in range(size)]
    random.shuffle(sample_list)
    return sample_list

def split(input_list):

    # returns back the original input if it's a single element (stops the recursion)
    if len(input_list) == 1:
        return input_list

    # set up the output list in the format of a split list
    output_list = [[],[]]

    # loop through the input elements
    for i in range(len(input_list)):

        # if the element is in the 1st half, add to output list position 0
        if i < ( (len(input_list) / 2) ):
            output_list[0].append(input_list[i])
        # if the element is in the 2nd half, add to output list position 1
        else:
            output_list[1].append(input_list[i])

    # recursively split the output lists
    output_list[0] = split(output_list[0])
    output_list[1] = split(output_list[1])

    return output_list

def merge(input_list):
    '''
    Merge and sort a split list
    '''
    
    #walk the array
    for item in input_list:
    
        if len(item[0]) == 1:
            u, v = (input_list[0], input_list[1])
            # start comparing elements
            if u < v:
                return [u, v]
            else:
                return [v, u]
        else:
            merge(input_list[0])

def merge_sort(input_list = []):

    return merge(split(input_list))

start_list = gen_sample_list(size=8)
print merge_sort(start_list)
