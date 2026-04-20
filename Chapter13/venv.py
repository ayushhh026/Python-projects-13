from functools import reduce
l =[1,2,3,4,5]

square = lambda x : x*x

sl=map(square,l)
print(list(sl))


def even(n):
    if(n%2==0):
        return True
    return False

onlyeven = filter(even,l)
print(list(onlyeven))

sum = lambda a,b: a+b
print(reduce(sum,l))