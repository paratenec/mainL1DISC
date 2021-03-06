import happy
import random


# Getting to know the user
name = str(input("Hello, what is your name?"))
print("Nice to meet you {}".format(name))

hobbies = str(input("Do you have any hobbies? If so what are they?"))

# Brief understanding of feelings
rating = float(input("On a scale from 1 to 10, with 1 being bad and 10 being good, how were you feeling today?"))


# Establishing the user's feelings
day1 = str(input("How are you feeling today?"))

day1 = day1.lower()

print("Today you were feeling {}".format(day1))

# Creating variety of responses
happylist = ["That's good!", "Yay that's awesome!", "Nice!", "That is great to hear!"]
sadlist = ["Oh no!", "That's terrible to hear!", "I hate to hear that"]
farewelllist = ["I hope you begin to feel better", "It was great to hear what you had to say", "Have a great rest of your day", "Goodbye {}".format(name)]


# Giving advice based on basic response
if day1 == 'happy':
    print(random.choice(happylist))
    happy_reasons = str(input("What made you feel like that?"))
    print("You said that the things that made you happy today were {}".format(happy_reasons))
    print("I suggest that you continue to do these things as sooner or later it will improve your mental health in a huge way.")
    print("Hopefully I could help.")
    print("Keep it up my friend.")

elif day1 == 'sad':
    print(random.choice(sadlist))
    sad_reasons = str(input("What is it that made you feel sad?"))
    print("The things you are saying made you sad are {}".format(sad_reasons))
    print("In my opinion I would say it is best to avoid these things as they will only deteriorate your mental health more.")
    print("It would be best for you to surround yourself with things that are quite opposite of this and things that make you happy.")
    print("I hope that my advice helps you.")
    print("Best of luck to you.")

# Giving advice based on a generalised response
else:
    print("Alright well thank you for telling me")
    happy_sad = str(input("Would you say this feeling is more on the happy side or the sad side?"))
    if happy_sad == 'happy':
        embrace = str(input("What are the things that made you feel like that?"))
        print("Some of the things that made you happy were {}.".format(embrace))
        print("You also mentioned whether or not you had any hobbies.")
        print("I recommend that you continue to do these hobbies if you enjoy them, and keep doing the things that make you happy.")
        print("Hopefully my advice is able to improve your overall feelings.")
        print("You are doing great my friend keep it up.")
    elif happy_sad == "sad":
        avoid = str(input("What were the things that made you feel sad?"))
        print("You think that the things that made you feel sad were {}".format(avoid))
        print("My advice is to try and avoid this happening and surround yourself with things that make you happy.")
        print("Hopefully this will help remove your negative feelings and improve your wellbeing overall.")
        print("Good luck my friend.")

# For statement of inputted data
data = [hobbies, day1]

for x in data:
    print("These are the things you enjoy doing and/or how you are feeling; {}".format(x))

# Creating farewell function
def farewell():
    print(random.choice(farewelllist))

farewell()
