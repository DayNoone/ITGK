import math
def polynom(x):
    y = math.e**-x**2
    return y

def simpson(func,a,b,d):
    diff = b-a/d
    S = polynom(a)
    
    for length in range(1,d,2):
        delta_x_1 = diff*length
        S += 4*polynom(delta_x_1)
        
    for length in range(2,d-1,2):
        delta_x_2 = diff*length
        S += 2*polynom(delta_x_2)

    S += polynom(a)
    S_ut = (diff/3)*S
    return S_ut

print(simpson(1,0,1,1000))

def simpsons_error(func,a,b,error):
    
