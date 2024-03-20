# Assignmnet 2 Nested if

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

# Task 2

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
if place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("Good choice!")
    elif action == "proceed in the dark":
        print("You crazy!")
else:
    print("You find a hidden treasure!")

# Task 3

place = input("Choose a place: forest, cave, or mountain? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
if place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("Good choice!")
    elif action == "proceed in the dark":
        print("You crazy!")
if place == "mountain":
    pass
else:
    print("You find a hidden treasure!")

# The Event Planner

attendees = input("Enter number of attendees: ")
food_choice = input("Would you like vegetarian food? (y/n) : ")
attendees_int = int(attendees)
venue = "large hall" if attendees_int > 100 else "conference room"
audio_system = "Dolby Digital" if attendees_int > 100 else "Bluthooth"
projector = "1000 inch 4k" if attendees_int > 100 else "500 inch 4k"
print('\n')
if food_choice == "y":
    print("We recommend Veggie Delight Caterers!")
else:
    print("We recommend Gourmet Meals Caterers!")
print(venue)
print(audio_system)
print(projector)