#initiate a class
class employee:
    #special function/special method/ dunder method- constructer 
    def __init__(self):
        print(id(self))
        print("Started executed attributes or data")
        self.id=123
        self.salary= 50000
        self.designation="SDE"
        print("Attributes or data have been initiated")

    def travel(self, destination):
        print("This travel method was called manually")
        print("Employee is now traveling to", destination)

#Create the instatance or object of the class
sam= employee()
#print(sam.salary)
#sam.travel("kerala")
print(type(sam))
print(id(sam))
sam.name= "Sam Kumar" # We can create the functionality outside of the class as well 
print(sam.name)
