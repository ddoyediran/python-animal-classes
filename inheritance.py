class Animal:
  legs = 0
  sound = "say something!"
  def __init__(self, name, owner):
    self.name = name
    self.owner = owner
   
  def speak(self):
    print(self.sound)


# Class of Dog    
def Dog(Animal):
  sound = "wolf!"
  legs = 4
  #def speak(self):
    #print("woof!)
    
  def fetch(self, item):
    print("I fetched " + str(item))
    
 
# Class of Chicken
def Chicken(Animal):
  sound = "cluck!"
  legs = 2
  
  #def speak(self):
    #print("cluck")
  
# Class of Goldenretrieval that takes an instance of dog 
def Goldenretriever(Dog):
  breed = "Golden retriever"


 

class Account:
  """A bank account that has a non-negative balance."""
  interest = 0.02
  def __init__(self, account_holder):
    self.balance = 0
    self.holder = account_holder
    
  def deposit(self, amount):
    """Increase the account balance by amount and return the new balance."""
    self.balance = self.balance + amount
    return self.balance
  
  def withdraw(self, amount):
    """Decrease the account balance by amount and return the new balance."""
    if amount > self.balance:
      return 'Insufficient funds'
    self.balance = self.balance - amount
    return self.balance
  


  
  
