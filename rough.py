list1= [1,3,4,19]
my_str= "mlops playlist"
my_int= 155
#print(type(list1))
#print(type(my_int))
#my_str= my_str.capitalize()
#print(my_str)

# function Vs Method below

from oop_project import chatbook
user1= chatbook()
print(user1.id)

chatbook.set_id(10)
user2=chatbook()
print(user2.id)





#user1=chatbook()
#a1= len(list1)
#print(a1)

#print(user1.id)
#user2=chatbook()
#print(user2.id)

#user3=chatbook()
#print(user3.id)

#user1=chatbook()
#user1.send_message()  # how to call method through object
#print(user1.name)

# Getter and setter
#print(user1.get_name())
#user1.set_name("Agent Vinod")
#print(user1.get_name())
