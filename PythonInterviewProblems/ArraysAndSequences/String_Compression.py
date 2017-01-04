def compress(s):

    output = []
    
    s += " "
    
    value = s[0]
    i = 1
    j = 1

    while i < len(s):
        
        if s[i] == value:
            j += 1
        else:
            append_string = value + str(j)
            output.append(append_string)
            value = s[i]
            j = 1
        i += 1
    

    return "".join(output)

print compress('AAAaaa')
