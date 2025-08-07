# class Person:
#     def __init__(self,name):
#         self.name=name

#     def printname(self):
#         print(self.name)

# person=Person("aarya")
# person.printname()




#inheritence
class Vehicle:
    def move(self):
        print("Moving")
class Car(Vehicle):
    def wheel(self):
        print("4 wheels")
c=Car()
c.move()
c.wheel()



