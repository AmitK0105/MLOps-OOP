#class Animal:
    #def __init__(self, name):
        #self.name= name
        

    #def speak(self):
        #print(self.name ,"makes a sound")


#animal= Animal("Generic Animal")
#animal.speak()

# Derived class
#class Dog(Animal):

    #def __init__(self):
        #self.behaviour= "Friendly"
        
    #def speak(self):
        #print(" Buddy barks & He is very", self.behaviour)

#object of child class
#dog= Dog("Buddy")
#dog.speak()

#constructor overloading
#dog= Dog()
#dog.speak()

# Super

class Animal:
    def __init__(self):
        self.name= "Buddy"

    def speak(self):
        print(self.name, "makes a sound")
        

#Derived Class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed =breed

    def speak(self):
        super().speak() # call the parent class method
        print((self.name) ,"barks it is a", (self.breed))


dog= Dog("Golden Retriver")
dog.speak()