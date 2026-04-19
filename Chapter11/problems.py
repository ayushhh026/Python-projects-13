'''class TwoDVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"The vector is {self.i}i and {self.j}j ")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.k=k
    def show(self):
        print(f"The vector is {self.i}i and {self.j}j and {self.k}k ")

a=TwoDVector(1,2)
a.show()
b=ThreeDVector(3,4,5)
b.show()
'''

'''class Employee:
    salary = 234
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return(self.salary + self.salary*(self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary)-1)*100


e=Employee()
e.salaryAfterIncrement=280.8
print(e.increment)'''


class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i 
    def __add__(self,c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self,c2):
        pass
    

    def __str__(self):
        return f"{self.r} + {self.i}i "
    
    def __len__(self):
        return 2

c1 = Complex(1,2)
c2 = Complex(23,4)
print(c1+c2)
print(len(c1))