import math
def is_prime(primtall):
    kvad = math.floor(math.sqrt(primtall))
    if(primtall%2==0):
        return False
    
    for i in range(3,kvad+1,2):
        if(primtall%i==0):
            return False
    return True

print(is_prime(float(input("Primtallstest: "))))
