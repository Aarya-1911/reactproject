class Person:
    def __init__(self,name):
        self.name=name

    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
person=Person("aarya")
person.setName("aarya k")
person.getName()
