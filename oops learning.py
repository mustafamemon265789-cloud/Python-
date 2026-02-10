# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("Adding New Student In Database")

#     def welcome(self):    
#         print("Welcome",self.name)
    
#     def get_marks(self):
#         return self.marks
    
# s1 = Student("Alice",56)
# print(s1.name,s1.marks)

# s2 =  Student("Bob",89)        
# print(s2.name)
# print(s2.get_marks())
# s2.welcome()        

# class Student():
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("HELLO",self.name,"Your Average Marks Is:",sum/3)   
#     @staticmethod    
#     def hello():
#         print("Hello")
    
# s1 = Student("Ali",[88,72,65])           
# s1.get_avg()

# s1.name = "Batman"
# s1.get_avg()

# # Abstraction
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch=False

#     def start(self):
#         self.acc = True
#         self.brk = False
#         self.clutch = False
#         print("Car Started...") 
# car1 = Car()
# car1.start()           

# Encapsulation
# class Account:
#     def __init__(self,bal,acc):
#         self.balance = bal
#         self.account_no = acc

#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs.",amount,"was debited")
#         print("Total Balance",self.get_balance)

#     def credit(self,amount):
#         self.balance += amount
#         print("Rs.",amount,"Was Credit")
#         print("Total Balance",self.get_balance)

#     def get_balance(self):
#         return self.balance    
    
# acc1 =  Account(10000,12345)
# print(acc1.balance)
# print(acc1.account_no)

# # Input se amount lena
# amount = int(input("Enter The Amount You Want To Debit? "))
# acc1.debit(amount)

# # Credit ke liye
# amount2 = int(input("Enter The Amount You Want To Credit ? "))
# acc1.credit(amount2)        

# Del Keyword

# class Computer:
#     def __init__(self,model):
#         self.model= model
# c1 = Computer("HP,Gen 10,Core i8") 
# del c1     
# print(c1)  

# Private Class

# class Person:
#     __name = "Majid"

#     def __hello(self):
#         print("Hello Person!")

#     def welcome(self):
#         self.__hello()    

# p1 = Person()
# print(p1.welcome())

# class Car:
#     @staticmethod
#     def start():
#         print("Engine Started...")

#     @staticmethod
#     def stop():
#         print("Engine Stop...")

# class ToyotaCar(Car):
#     def __init__(self,Brand):
#         self.brand = Brand
# car1 = ToyotaCar("Fortuner")   
# car2 = ToyotaCar("Prius") 

# class Carolla(ToyotaCar):
#     def __init__(self,type):
#         self.type=type
        
# car1 = Carolla("diesel")        
# car1.start()
# Multiple Inheritense
# class A:
#     varA = "Welcome To Toyota Fortuner"

# class B:
#     varB = "This car is so amazing"

# class C(A,B):
#     varC = "Here's The feature of car"
# c1 = C()
# print(c1.varC) 
# print(c1.varB)
# print(c1.varA)   
#super methode
# class Car:
#     def __init__(self,type,start):
#         self.type=type
#         self.start=start

#     def start():
#         print("Engine Started...")

#     @staticmethod
#     def stop():
#         print("Engine Stop...")

# class ToyotaCar(Car):
#     def __init__(self,Brand,type,start):
#         self.brand = Brand
#         super().__init__(type)
#         self.type= type
#         super().__init__(start)

# car1 = ToyotaCar("Fortuner","electric")   
# car2 = ToyotaCar("Prius","electric") 
# print(car1.type)
# print(car1.start)
