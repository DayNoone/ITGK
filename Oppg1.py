import math
def polynom (x):
    y = x**5-4*x**3+10*x**2-10
    return y

def polynom_derivative (x):
    y = 5*x**4-12*x**2+20*x
    return y

def newton (func,deriv,a,threshold,max_iterations):
    a_gammel = a
    for iterations in range(0,max_iterations):
        a = a_gammel - (polynom(a_gammel)/deriv(a_gammel))
        if(math.fabs(a_gammel-a) < threshold):
            print(format(a,".6f"))
            break
        if(iterations == max_iterations-1):
            print("False")
        a_gammel = a
        
print(newton(polynom,polynom_derivative,-3,0.000001,20))
            
    
    
