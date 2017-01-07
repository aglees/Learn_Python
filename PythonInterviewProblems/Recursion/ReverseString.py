def reverse(s):

    # must use recursion
    if len(s) == 0:
        return ""

    return  s[len(s)-1] + reverse(s[:len(s)-1])

def reverse2(s):

    # must use recursion
    if len(s) <= 1:
        return s

    return reverse(s[1:]) + s[0]

print(reverse('hello world'))
print(reverse2('hello world'))