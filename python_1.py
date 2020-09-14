# x = 15
# #Python sees 15 and create it , what am I going to assign it to? oh, x
# price = 9.99
# # creating a value with floating point and assiging it to price

# discount = 0.2

# result = price * (1-discount)
# # that is a code to calculating a disscount

# print(result)
# # show user something in the console

# string class str
# name = "Rolf" #creating a string "Rolf" and assigning it for name
# print(name)
# print(name *2) #Multiplying strings

# a = 25 #Python does not create the value 25, it moves it, values 0-255 allready exist in the system
# b = a # both a and be are names for 25 
# print(a)
# a = 32 # b is 25 and a is 32
# print(b)

# formatting

# name = "Bob"
# print(f"Hello, {name}")



# name = "Rolf"


# name = "Bob"

# greeting = "Hello, {}"
# with_name = greeting.format("rolf")

# name = "dog"

# print(with_name)


# longer_phrase = "Hello, {}. Today is {}."

# formatted = longer_phrase.format("Rolf", "Monday")
# print(formatted)

# name = input("Enter your name: ")
# x = 23094.0144392
# print(f"{x/2304200:.3%}")
# print("{:.3f}".format(x))

#inputs always gives u back a string
# size = input("fuck off: ")
# print(int(size))

# age = input("what is your age: ")
# years = int(age)
# age_month = years * 12
# print(f"you are {age} years old and {age_month} months old")

# lists tuples and sets

# l = ["Bob", "Rolf", "Anne"]
# t = ("Bob", "Rolf", "Anne") #Tuple cannot be modified ('tuple' object has no attribute 'append')
# s = {"Bob", "Rolf", "Anne"} #The order can change at any moment

# print(l[0])

# l.append("just another element")
# print(l)

# l.remove("Bob") # fk off boob
# print(l)

# s.add("just another element don't mind him")
# print(s)

# # list is the most standard collection when u can add/modify , tuple you can't add or modify, set has no order

# friends = {"Bob", "Rolf", "Anne"}
# abroad = {"Bob", "Anne"}

# local_friends = friends.difference(abroad)
# print(local_friends)

# local = {"Shir", "Hadasa", "Michal"}
# abroad = {"Shmulik", "Colin", "Tim", "Avial", "Yael"}

# total_family = local.union(abroad)
# print(total_family)

# art = {"Bob", "Jen", "Rolf", "Charlie"}
# science = {"Bob", "Jen", "Adam", "Anne"}

# both = art.intersection(science)
# print(both)
# my_tuple = 15,6 
# print(type(my_tuple))
# print(my_tuple)

# print( True == 1)
# print( True is 1)

# day_of_week = input("What day of the week is it today? ").lower()
# if day_of_week == "monday" :
#     print("Have a great start to your week!")
# elif day_of_week == "tuesday":
#     print("It''s Tuesday.")
# else:
#     print("Full speed ahead!")
# print("This always runs.")

# Learning about the in keyword
# in looks into membership

# friends = [ "Bob", "Ross", "Jen"]
# print ("Jen" in friends)

# movies_watched = {"The matrix", "Green Bokk", "Her"}
# user_movie = input("Enter something you've watched recently: ")
# print(user_movie in movies_watched)

# if statements with in keyword


# movies_watched = {"The matrix", "Green Bokk", "Her"}
# user_movie = input("Enter something you've watched recently: ")

# if user_movie in movies_watched:
#     print(f"I've watched {user_movie} too!")
# else:
#     print("I haven't watched that yet.")

# number = 7
# user_input = input("Enter y if you want to play: ").lower()

# if user_input == "y":
#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print("You guessed correctly!")
#     elif abs(number - user_number) == 1:
#         print("You were off by one.")
#     else:   
#         print("Sorry, it's wrong!")

#Loops in python

# number = 7


# while True:
#     user_input = input("would you like to play? (Y/n) ")
#     if user_input == "n":
#         break
#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print("You guessed correctly!")
#     elif abs(number - user_number) == 1:
#         print("You were off by one.")
#     else:   
#         print("Sorry, it's wrong!")

# friends = ["Rolf", "Jen", "Bob", "Anne"]
# for friend in range(4):
#     print(f"{friends[friend]} is my friend.")

# grades = [35,67,98,100,100]
# total = sum(grades)
# avg = total / amount
# print(avg)

# numbers = [1, 3, 5]
# doubled = [x * 2 for x in numbers]
# print(doubled)

# friends = ["Rofl", "Sam", "Samantha", "Saurabh", "Jen"]
# starts_s = [friend for friend in friends if friend.startswith("S")]
# print("friends: ", id(friends), "starts_s: ", id(starts_s))

# print(starts_s)

#Dictionaries are another structure in python like lists sets and tuples that allows us to interact with data in a certain way
# friend_ages = {"Rolf" : 24, "Adam" : 30, "Anne" : 27}

# friend_ages["Rolf"] = 20

# print(friend_ages["Adam"])

# friends = [
#     {"name" : "Rolf", "age" : 24},
#     {"name" : "Adam", "age" : 30},
#     {"name" : "Anne", "age" : 27},
# ]

# print(friends[1]["name"])



# student_attendance = {"Rolf" : 96, "Bob" : 80, "Anne" : 100}
# for student  in student_attendance.items():
#     print(f"{student}" )
#     print("sup")


# student_attendance = {3 : 96, 4 : 80, 3 : 100}
# print(dict.fromkeys(student_attendance))

# student_attendance = {"Rolf" : 96, "Bob" : 80, "Anne" : 100}
# total_attendance = sum(student_attendance.values())
# avg_attendance = total_attendance / len(student_attendance.values())
# print(avg_attendance)

# student_attendance = {"Rolf" : 96, "Bob" : 80, "Anne" : 100}
# print(list(student_attendance.items()))

# for t in student_attendance.items():
#     print(t)
# print(f"{student}: {attendance}")

# people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]
# for name, age, profession in people:
#     print(f"Name: {name}, Age: {age}, Profession: {profession}")

# person = ("Bob", 42, "Mechanic")
# name, _, _ = person
# print(name)

# *head, tail = [1,2,3,4,5]
# print(*head)
# print(tail)

# def hello():
#     print("Hello!")

# hello()

# def user_age_in_seconds():
#     user_age = int(input("Enter your age: "))
#     age_seconds = user_age * 365 * 24 * 60 * 60
#     print(f"your age in seconds is {age_seconds}.")

# user_age_in_seconds()

# Function arguments argument and parameters
# def add(x,y):
#     print(x + y)
#     return x + y

# add(5,3)

# def say_hello(name, surname):
#     print(f"Hello!, {name} {surname}")



# say_hello(surname = "Bob",name =  "Smith") #names keyword arguments

# def divide(dividend, divisor):
#     if divisor != 0:
#         print(dividend / divisor)
#     else:
#         print("You fool!")

# divide(dividend = 15, divisor=0) #keyword arguments must go after positional arguments

#default paramater values
# def add(x,y=7):
#     print(x+y)


# add(5,8)
# functions return None, thats what they do by default
# print("hello")

# lambda function is a function that does not have a name and only used to return values

# print((lambda x, y : x + y) (5,7))

# def double(x):
#     return x *2

# sequence = [1, 3, 5, 9]
# # doubled = [x * 2 for x in sequence] # slightly faster 
# # doubled = map(double, sequence) #apply the function double to each item in sequence

# doubled = [x *2 for x in sequence]
# print(doubled)

# users = [                                             #Making a login in the game
#     (0, "Bob", "password"),
#     (1, "Rolf", "bob123"),
#     (2, "Jose", "longp4assword"),
#     (3, "username", "1234"),

# ]

# username_mapping = {user[1]: user for user in users}
# # print(username_mapping["Bob"])
# username_input = input("Enter your username: ")
# password_input = input("Enter your username: ")

# _ , username , password = username_mapping[username_input]

# if password_input == password:
#     print("Your details are correct!")
# else:
#     print("Your details are incorrect.")

#Unpacking arguments
# def multiply(*args):
#     print(args)
#     total = 1
#     for arg in args:
#         total = total * arg
#     return total


# print(multiply(1, 3, 5))

# def add(x,y):
#     return x + y

# nums = [3,5]
# add(*nums)
print("this")