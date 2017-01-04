def rev_word(s):
    
    lst = s.split()

    output = []
    for i in range(len(lst)-1,-1,-1):
        output.append(lst[i])

    mystring = " ".join(output)
    
    return mystring

def rev_word2(s):
    return " ".join(reversed(s.split()))

def rev_word3(s):
    return " ".join(s.split()[::-1])

print (rev_word('Hi John,   are you ready to go?'))
print (rev_word2('Hi John,   are you ready to go?'))
print (rev_word3('Hi John,   are you ready to go?'))