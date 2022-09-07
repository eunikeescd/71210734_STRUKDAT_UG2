
import time

#iteratif
def deret_ajaib(n):
    if (n <= 5):
        return n
    else:
        return ((n-2)+(n//2))
        
#rekursif
def deret_ajaib(n):
    der = [1,2,3,4,5]
    if n in der:
        return n
    else:
        return (deret_ajaib(n-2)+deret_ajaib(n//2))


start = time.time()
print(deret_ajaib(9))
end = time.time()
print('Rekursif',' n =',n,end-start,'detik')
