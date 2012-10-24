def revers(a):
    b=""
    for i in range(len(a)):
        b += a[-i-1]
    print(b)
revers("heia")
