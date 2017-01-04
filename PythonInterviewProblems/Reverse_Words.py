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

def rev_word4(s):

    # remove leading and trailing white space
    u = v = 0
    for u in range(len(s)):
        if s[u] != " ":
            break

    word = s[::-1]

    for v in range(len(word)):
        if word[v] != " ":
            break

    output = []
    for z in range(u, len(s) - v):
        print s[z]

    return output

def rev_word5(s):

    spaces = [" "]
    words = []
    i =  0
    length = len(s)

    while i < length:

        if s[i] not in spaces:
            
            word_start_index = i
            
            while (i < length) and s[i] not in spaces:
                i += 1
            
            words.append(s[word_start_index:i])
        
        i += 1

    return " ".join(reversed(words))
        



# print (rev_word('Hi John,   are you ready to go?'))
# print (rev_word2('Hi John,   are you ready to go?'))
# print (rev_word3('Hi John,   are you ready to go?'))
print (rev_word5('Hi John,   are you ready to go?'))
