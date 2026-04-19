'''class Em:
    company="itc"
    def show(self):
        pass
class Coder:
    language="py"
    def languagesss(self):
        print(f"the language you choosed is {self.language}")

class Programmer(Em, Coder):
    company="ITC info"
    def read(self):
        pass

a=Em()
b=Programmer()
b.languagesss()

print(a.company,b.company)'''

'''class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a=1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of programmer")
    b=2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of manager")
    c=3

o= Manager()
print(o.a,o.b,o.c)'''


class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"the value of a is {cls.a}")
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name (self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

e=Employee()
e.a=45

e.name="ayush shetty"
print(e.fname, e.lname)
e.show()
    