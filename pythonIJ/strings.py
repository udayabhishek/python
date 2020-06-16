print("hello world")
print("mac" + "book")
greeting = "Hi"
# name = input("please enter your name ")
# print(greeting+ " " + name)
splitlines = """this string has been
              in
     seveal
       lines"""
print(splitlines)
# when backslash comes in path
# print("\User\time\notes.txt") #this will give error

print("\\User\\time\\notes.txt")  #using escape character

print(r"\User\time\notes.txt") #using 'r' for raw string


age = 21
print(age)
print(type(age))
age = "21 years"
#  ("hi " + type(age)) # this will give error, not the same type



# ******Operators*******
a=11
b=3

print(a/b) #4.0
print(a//b)  #4 integer division, rounded down towards minus infinity
print(a % b) # remaminder

# for i in range(1, a/b): this will give error
#     print(i)

for i in range(1, a//b):
    pass

parrot = "norwegain blue"
print(parrot)
print(parrot[3])

print(parrot[-1])
print(parrot[-2])
print(parrot[-12])
print(1_0_0)


numbers = list(range(1,10))
print(numbers)

numbers = list(range(1,10, 2)) #'2' is step to increment numbers
print(numbers)

# squares of all the numbers i the list
for num in numbers:
    print(num**2, end=' ')


