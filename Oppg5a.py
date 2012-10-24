def sammenlign(a,b):
    for x in range(len(a)):
        if(a[x]!=b[x]):
            return False
    return True
print(sammenlign("hei","hei"))
print(sammenlign("hei","hai"))
