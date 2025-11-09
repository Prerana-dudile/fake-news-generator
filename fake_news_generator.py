# Fake News Generator
# Description: A fun beginner Python project that randomly
#              generates funny or fake headlines for learning.

import random 

subjects = [
    "Shahrukh khan",
    "Virat kohli",
    "A Mumbai cat",
    "A group of monkeys",
    "auto rikshaw driver from Delhi"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a plote of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"
]

print("Welcome to the Fake News Generator!")
print("This program is for fun and learning only.")


while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {places_or_thing}!"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no)").strip()
    if user_input.lower() == "no":
        break

print("\nThanks for using the Fake News Headline Generator.Have a fun day")