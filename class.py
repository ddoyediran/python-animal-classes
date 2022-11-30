class Animal():
  legs = 0
  sound = "say something!"
  def __init__(self, name, owner):
    self.name = name
    self.owner = owner
   
  def speak(self):
    print(self.sound)


# Class of Dog    
class Dog(Animal):
  sound = "wolf!"
  legs = 4
  #def speak(self):
    #print("woof!)
    
  def fetch(self, item):
    print("I fetched" + str(item))
    
 
# Class of Chicken
def Chicken(Animal):
  sound = "cluck!"
  legs = 2
  
  #def speak(self):
    #print("cluck")
  
# Class of Goldenretrieval that takes an instance of dog 
def Goldenretriever(Dog):
  breed = "Golden retriever"



