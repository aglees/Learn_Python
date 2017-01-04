def rev_word(s):
    
    lst = s.split()

    output = []
    for i in range(len(lst)-1,-1,-1):
        output.append(lst[i])

    mystring = " ".join(output)
    
    return mystring

print (rev_word('Hi John,   are you ready to go?'))