place = input("Choose a place: forest/cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("you found a bird's nest")
    elif action == "cross a river":
        print("you found a boat")
else:
    print("you found a hidden treasure")
if place == "cave":
    action = input("light a torch? or proceed in the dark?")
    if action == "light a torch":
        print("you are afraid of the dark")
elif if action == "proceed in the dark":
    print("you are one brave man")

attendees = input("Enter number of attendees:")
venue = ("large hall") if int(attendees) > 100 else ("conference room")
venue = ("large hall") if int(attendees) > 100 else ("conference room") if int(attendees) < 100 else ("audio room")
print(venue)
food = input("do you want (vegan/meat)")
if food == "vegan:":
    print("i think you should try the Veggie Delight Caterers")
else:
    print("i would try Gourment Meals Caterers")
