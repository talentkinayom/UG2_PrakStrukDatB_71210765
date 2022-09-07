import time
def deretajaib(n):
    if n<6 :
        return n
    else:
        return deretajaib(n-2)+deretajaib(n//2)

def deret(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
print(deret(5))