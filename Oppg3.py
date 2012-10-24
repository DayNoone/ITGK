import math
def pytagoras(x_1,x_2,y_1,y_2):
    py = math.sqrt((((x_1-x_2)**2)+((y_1-y_2)**2)))
    return py
    
def perimeter(x,y):
    lengde = 0
    for i in range(0,len(x)):
        if(i == len(x)-1):
            lengde += pytagoras(x[i],x[0],y[i],y[0])
        else:
            lengde += pytagoras(x[i],x[i+1],y[i],y[i+1])
         
    return lengde
        
print(perimeter([1,2,4,5,3],[2,4,5,4,1]))
