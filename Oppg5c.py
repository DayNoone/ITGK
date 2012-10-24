def palindrom(a):
    forste = a[0::2]
    siste = a[1::2]
    #if(
    siste_rev = ""
    for i in range(len(siste)):
        siste_rev += siste[-i-1]
    for x in range(len(forste)):
        if(forste[x]!=siste_rev[x]):
            return False
    return True

print(palindrom("aabaa"))
print(palindrom("anttna"))
