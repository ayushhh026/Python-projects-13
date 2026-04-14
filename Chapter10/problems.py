'''class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name= name
        self.salary = salary
        self.pincode = pincode
p = Programmer("ayush",123344,40001)
print(p.name,p.salary,p.pincode,p.company)'''

'''class Calci:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"sqaure is {self.n*self.n}")
    def cube(self):
        print(f"sqaure is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"sqaure is {self.n**1/2}")
a=Calci(4)
a.square()
a.cube()
a.squareroot()'''
from random import randint
class Train:
    def __init__(slf,Trainno):
        slf.Trainno=Trainno
    def book(self,fro,to):
        print(f"Ticket is booked in train no: {self.Trainno} from {fro} to {to}")
    def getStatus(self):
        print("train is running successfully and on time")
    def getFare(self, fro, to):
         print(f"Ticket fare in in train no: {self.Trainno} from {fro} to {to} is {randint(222,2343)}")
t= Train(12344)
t.book("mumbai","manglore")
t.getStatus
t.getFare("mumbai","manglore")
