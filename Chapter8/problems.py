#sum of first n natrual 1+2+3+n
'''
def sum(n):
    if(n==1):
        return 1
    return n + sum(n-1)
n=int(input("Enter a n "))
print(sum(n))
'''

#remove item for list and strip

"""def rem(l,word):
    n=[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n    
    
l = ["Harry","Ayush","an","sohan","Rohan"]

print(rem(l,"an"))
    """

def multiply(n):
    for i in range (1,11):
        print(f" {n} x {i} = {n*i}")
multiply(5)