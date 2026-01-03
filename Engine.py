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
# print(num[-1], num[-2])+
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