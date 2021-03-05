print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lowercase_1 = name1.lower() + name2.lower()

t = lowercase_1.count("t")
r = lowercase_1.count("r")
u = lowercase_1.count("u")
e = lowercase_1.count("e")

true = t + r +u +e

l = lowercase_1.count("l")
o = lowercase_1.count("o")
v = lowercase_1.count("v")
e = lowercase_1.count("e")

love = l+o+v+e

true_love = str(true) + str(love)

true_love_int = int(true_love)

if true_love_int < 10 and true_love_int > 90:
  print(f"Your score is {true_love_int}, you go together like coke and mentos.")
elif true_love_int > 40 and true_love_int < 50:
  print("Your score is {true_love_int}, you are alright together.")
else:
  print(f"Your score is {true_love_int}.")
