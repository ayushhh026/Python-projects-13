'''l = [1,2,3,4,4,57,8,9,]

for i,item in enumerate(l):
    if(i==2 or i==4 or i ==6):
            print(item)'''

'''
n = 5

table = [n*i for i in range(1,11)]
print(table)'''

'''try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a/b)
except ZeroDivisionError as v:
    print("infinite")
'''

n = int(input("ENter a number "))

table = [n*i for i in range(1,11)]
with open ("table.txt", "a") as f:
    f.write(f"Table of {n}:  {str(table)}  \n")