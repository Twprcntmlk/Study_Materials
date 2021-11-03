# Getter and Setter in Python
# - We use getters & setters to add validation logic around getting and setting a value.
# - To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.

class Location:
     def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

     # function to get value of _age
     @property
     def loc(self):
         print("getter method called")
         return [self.x, self.y]

     # function to set value of _age
     @loc.setter
     def loc(self,loc):
        print("setter method called")
        self.x, self.y =loc

     @loc.deleter
     def loc(self):
        print("deleter method called")
        self.x = self.y =0

     # function to delete _age attribute
    #  @age.deleter
    #  def age(self):
    #      del self._age

    #  age = property(get_age, set_age, del_age)

test=Location()
test.loc = 100,101
print(test.loc)
test.loc = 102,103
print(test.loc)
# del test.loc
print(test.loc)

print(test.loc)

#instance methos operate on the instance


#class methods are alternate constructors
raise_amt =1.04

@classmethod
def set_raise_amt(cls, amount):
   cls.raise_amt= amount


Employee.set_raise_amt(1.05)   ====     Employee.raise_amt = 1.05


# set
#static methods  which do not operate on the instance or the class
