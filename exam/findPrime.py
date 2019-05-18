
def isPrime(n,a):
    if n<2:
        return False
    if n==a:
        return True
    if n%a==0:
        return False
    return isPrime(n,a+1)

list=[]
i=2
while 1:
    if isPrime(i,2):
        list.append(i)
    i+=1
    if list.__len__() == 100:
        break
print(list)
