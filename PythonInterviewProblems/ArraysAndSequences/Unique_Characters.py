from collections import defaultdict

def uni_char(s):
        
    d = defaultdict()

    for item in s:
        if d.has_key(item):
            return False
        d[str(item)] = 1
    
    return True

def uni_char2(s):

    return len(set(s)) == len(s)

def uni_char3(s):
    
    char = set()
    
    for let in s:
        if let in char:
            return False
        else:
            char.add(let)
    return True

print (uni_char('abcdefg'))
print (uni_char2('abcdefg'))
print (uni_char3('abcdefg'))