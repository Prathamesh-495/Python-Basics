dummy = "hello world"
print(dummy)
print(type(dummy))

name = input("enter your name :")
print(name)
print(type(name))

text = input("Enter some text : ")
print(text.upper())
print(text.lower())
print(text.title())
print(text.find('e'))
print(text.count('a'))
print(text.replace('a','@'))
print(len(text))

x = int(input("Enter number within range 10 : "))
print(x>=3 and x<=10)