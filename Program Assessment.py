import happy
import sad

# Getting to know the user
name = str(input("Hello, what is your name?"))
print("Nice to meet you {}".format(name))

age = int(input("To help adapt the advice to your needs, what is your age?"))

hobbies = str(input("Do you have any hobbies?"))

# Establishing the user's feelings
day1 = str(input("How are you feeling today?"))

print("Today you were feeling {}".format(day1))

# Gathering further information
if day1 == happy:
    print("That is great to hear")
    print("What made it so good?")

if day1 == sad:
    print("That's no good")
    print("Could you please explain further?")

detail1 = str(input("Please go into further detail"))

