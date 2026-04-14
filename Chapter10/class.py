class Employee:
    language = "py"
    salary = 120000000

    def __init__(self,name,language,salary):
        self.name=name
        self.language=language
        self.salary= salary
        print("I am creating an object constructor")
    def getInfo(self):
        print(f"The language is {self.language}")

    @staticmethod
    def greet():
        print("Hello ji")
    
    
ayush = Employee("Ayush","C++",123456)
ayush.name="Ayush"
ayush.getInfo()
ayush.language="Javscript"
ayush.greet()
print(ayush.name, ayush.language, ayush.salary)
