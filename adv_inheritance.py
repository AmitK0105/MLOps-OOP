# Single or Basic Inheritance

#class parent:
    #def __init__(self, name):
        #self.name=name
        
    #def greet(self):
        #print("Hello my name is ", self.name)

#class child(parent):
    
    #def play(self):
        #print(self.name, "is playing")


#kid= child("Alice")
#kid.greet()
#kid.play()

#---------------------------------------------------------------------------------------------------------------------------
#Multilevel Inheritance

#Base Class
# class Grandparents:
#     def __init__(self, name):
#         self.name= name
        
#     def tell_strory(self):
#         print(self.name, "tells a strory")

# #Intermediate class
# class parent(Grandparents):
#     def work(self):
#         print(self.name, "is working")

# class child(parent):
#     def play(self):
#         print(self.name, "is playing well")


# kid= child("Charlie")
# kid.tell_strory()
# kid.work()
# kid.play()

#Hierarchycal Inheritance

# class Parents:
#     def __init__(self, name):
#         self.name= name
        
#     def greet(self):
#         print("Hello my name is", self.name)

# # Derived class
# class child(Parents):
#     def play(self):
#         print(self.name, "is playing")

# class child1(Parents):
#     def study(self):
#         print(self.name, "is studying")

# #create instance of child and child1

# kid= child("Tom")
# kid1= child1("Dave")

# kid.greet()
# kid.play()


# kid1.greet()
# kid1.study()

#----------------------------------------------------------------------------------

#Multiple inheritance & Diamond Problem

class A:
    def __init__(self, name):
        self.name= name

    def greet(self):
        print("Hello from A", self.name)

class B(A):
    def greet(self):
        print("Hello from B", self.name)
        super().greet()

class C(A):
    def greet(self):
        print("Hello from c", self.name)
        super().greet()

#Derived class

class D(B,C):
    def greet(self):
        print("Hello from D", self.name)
        super().greet()

#create an instance of D

di= D("Track")
di.greet()