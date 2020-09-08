import happy
import random


# Getting to know the user
name = str(input("Hello, what is your name?"))
print("Nice to meet you {}".format(name))

hobbies = str(input("Do you have any hobbies?"))

# Establishing the user's feelings
day1 = str(input("How are you feeling today?"))

print("Today you were feeling {}".format(day1))

happylist = ["That's good!", "Yay that's awesome!", "Nice!", "That is great to hear!"]
sadlist = ["Oh no!", "That's terrible to hear!", "I hate to hear that"]

# Gathering further information
if day1 == 'happy':
    print(random.choice(happylist))
    happy_reasons = str(input("What made you feel like that?"))

elif day1 == 'sad':
    print(random.choice(sadlist))
    print("What is it that made you feel sad?")



