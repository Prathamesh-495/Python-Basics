# dummy = "hello world"
# print(dummy)
# print(type(dummy))

# name = input("enter your name :")
# print(name)
# print(type(name))

# text = input("Enter some text : ")
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.find('e'))
# print(text.count('a'))
# print(text.replace('a','@'))
# print(len(text))

# x = int(input("Enter number within range 10 : "))
# print(x>=3 and x<=10)

# courses = ['ba','bcom','bsc','ma','mcom','msc']
# print(courses)
# print(courses[0])
# print(courses[1:3])
# print(courses[-1])

# courses.append('BE')
# print(courses)
# courses.insert(3,'ME')
# print(courses)

# new = ['11th','12th']
# courses.append(new)
# print(courses)
# courses.extend(new)
# print(courses)

# for items in courses:
#     print(items)


# # Tuple definition
# courses = ('ba', 'bcom', 'bsc')
# print(courses, type(courses))

# # Access elements
# print(courses[1], courses[3-1])
# print(courses[3:5], courses[-3:])

# # Functions: count() and index()
# courses = ('ba','bcom','bsc','bsc','ba')
# print(courses.count('bsc'), courses.index('bsc'))

# # Iterating tuples
# for item in courses:
#     print(item)
# for idx, item in enumerate(courses):
#     print(idx, item)

# # Length
# print(len(courses))

# # Mixed data types
# data = ('ba', 2, True, 'bsc')
# for item in data:
#     print(item, type(item))

# # Single-element tuple
# single1 = ('50')   # string
# single2 = ('50',)  # tuple
# print(type(single1), type(single2))

# # Combining tuples
# print(('a','b') + (1,2))
# print(('50',) + ('apple',) + ('mango','orange'))

# # Membership check
# fruits = ('apple','mango')
# print('mango' in fruits, 'mangoes' in fruits)

# # Max, Min
# print(max(2,1,3,7), min(2,1,3,7))

# # List → Tuple
# num_list = [1,2,3,4]
# num_tuple = tuple(num_list)
# print(num_list, num_tuple)

# # Negative indexing
# num = (1,2,3,4,5,6,7)
# print(num[-1], num[-2])
# print(num[6])

# # Tuple slicing
# courses = ('ba','bcom','bsc','be','ma','mcom','msc','me')
# print(courses[3:5], courses[3:], courses[:3], courses[-3:])


# # Dictionary Example
# student = {
#     "name": "Riya",
#     "age": 22,
#     "course": "B.Tech",
#     "year": 4
# }

# # Access
# print(student["name"])
# print(student.get("roll_no", "Not Assigned"))

# # Add / Update
# student["roll_no"] = 101
# student["age"] = 23
# student.setdefault("hobby", "Reading")

# # Delete
# student.pop("course")
# student.pop("non_exist_key", "No Key")
# del student["year"]
# # student.clear()  # Uncomment to empty the dictionary

# # Other functions
# print(student.keys())
# print(student.values())
# print(student.items())
# print(len(student))
# copy_student = student.copy()
# new_student = dict.fromkeys(["name","age","city"], "Unknown")

# # Looping
# for k, v in student.items():
#     print(k, ":", v)

# for k in student:
#     print(k)

# for v in student.values():
#     print(v)

# # Sorting by keys
# for k in sorted(student):
#     print(k, student[k])

# # Nested Dictionary
# classes = {
#     "class1": {"teacher": "Mr. A", "students": 20},
#     "class2": {"teacher": "Ms. B", "students": 25}
# }

# for cls, details in classes.items():
#     print(cls)
#     for k, v in details.items():
#         print(" ", k, "=", v)


# fruits = {"apple", "banana", "orange"}
# fruits.add("mango")
# fruits.update(["grapes", "kiwi"])
# fruits.remove("banana")
# fruits.discard("banana")
# popped_item = fruits.pop()
# all_cleared = fruits.copy()
# fruits.clear()

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}

# union_set = A | B
# intersection_set = A & B
# difference_set = A - B
# symmetric_diff = A ^ B

# union_method = A.union(B)
# intersection_method = A.intersection(B)
# difference_method = A.difference(B)
# sym_diff_method = A.symmetric_difference(B)

# for x in A:
#     print(x)

# for x in sorted(A):
#     print(x)

# if 3 in A:
#     print("Found 3")

# length = len(A)
# min_val = min(A)
# max_val = max(A)
# copy_set = A.copy()

# nums = [1,2,2,3,3,3]
# unique_nums = set(nums)
# letters = set("banana")



# def greet(name):
#     print(f'hello,good morning,{name}')
# greet('prathamesh')
# greet(11)

# def hello(name):
#     return (f'hello, {name}')
# print(hello('prathamesh'))

# def hi(name):
#     message = 'HI '+name
#     return message
# name = input("Enter your name : ")
# print(hi(name))

# def add(a,b):
#     return a+b
# a = int(input("enter val of a : "))
# b = int(input("enter val of b : "))
# print("sum = ",add(a,b))


# a = 33
# b = 200
# if b > a:
#   print("b is greater than a")


# n = int(input(" Enter a number to check:"))
# if n % 2 == 0:
#   print("It's an even number.")
# if n % 2 != 0:
#   print("It's an odd number.")
# if n == 0:
#   print("The number is neither even nor odd. Rather you entered Zero.")

# number = int(input("Enter the number?  "))  

# if number==30:  
#     print("The number you entered is: 30 ")  
# elif number==40:  
#     print("The number you entered is: 40") 
# elif number==50:  
#     print("The number you entered is: 50")
# else:  
#     print(" You have entered a random number other than 30, 40 and 50.") 


# x = 41

# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")


# courses = ['ba','bcom','bsc','be']
# for i in courses:
#     print(i)

# fruits = ('apple','mango','banana')
# for fruit in fruits:
#     print(fruit)

# company = {'name':'google','location':'usa','type':'search engine'}
# for key in company:
#     print(key,company[key])

# for id,item in enumerate(courses):
#     print(id,item)

# courses = ['ba', 'bcom', 'bsc', 'be']
# for item in courses:
#   print(item)
#   if item == 'bsc':                 # we wan't to break the loop when 'bsc' is reached
#     break
  
# courses = ['ba', 'bcom', 'bsc', 'be']
# for course in courses:
#   if course == 'bsc':
#     continue
#   print(course)

# nums = [11,23,30,43]  
# count = 0;  
# for item in nums:  
#     count = count + 1
# print("Total length - ",count)


# rows = int(input("Enter the rows  :"))    
# for i in range(0, rows+1):               
#     for j in range(i):                    
#         print("*", end='')               
#     print()    


# for i in range(5): # outer loop
#     for j in range(10, 20): # inner loop
#         print(i, j)

# num = [10,30,23,43,65,12]  
# sum = 0  
# for i in num:  
#     sum = sum + i     
# print("The sum is:",sum) 


# x = 1
# while x < 5:
#     print(x)       
#     x += 1

# while True:
#     name = input('Input name: ')
#     if name == 'pande':
#         break
#     print("Your name is:", name)

# i = 0  
# str1 = 'Beautiful'  
  
# while i < len(str1):   
#     if str1[i] == 't':   
#         i += 1  
#         break  
#     print('Current Letter :', str1[i])   
#     i += 1 


# class Employee:            
#     name = "John"          
#     age = 26

# emp = Employee()           
# type(emp)
# print(emp.name)    
# print(emp.age)


# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

    
#     def details(self):
#         print("Employee Name: ",  self.name)
#         print("Employee Age: ", self.age)
 

# emp1 = Employee("John", 26)         
# emp2 = Employee("Jane", 24)         

# emp1.details()
# emp2.details()


# class Rectangle:
#     def __init__(self, length, width ):
#         self.length = length
#         self.width = width
#     def area(self):
#         print(f"Length - {self.length}, Width - {self.width}")
#         return self.length * self.width

# first = Rectangle(5,2)
# print(first.area())


# class Dog:
#   def __init__(self, breed, age, color):
#     self.breed = breed
#     self.age = age
#     self.color = color
#   def details(self):
#     print(f"Breed - {self.breed}, Age - {self.age}, Color - {self.age} ")

# dog1 = Dog('Husky', 5, 'Blank')

# dog1.details()



import math
math.sqrt(4)

# But if you import sqrt() specifically, then you can access it just like that. 
from math import sqrt       
sqrt(4) 

math.log10(100)

from datetime import date, datetime
print(date.today())
today = date.today()
print(today)
print(today.day, today.month, today.year) 
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) 