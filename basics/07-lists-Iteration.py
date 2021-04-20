# Auto-indent - When typing python statements which end in a colon (for example if, for, while) then the prompt will change to three dots (...) and the cursor will be indented by 4 spaces.
# for-in loop - Iteration - for loop in the list
# .copy() - Mutability - copy method, makes the copy of the list
# .remove() - remove a certain value in the () of the list


# meeting.py

attendees = ['Ken', 'Alena', 'Treasure']
attendees.append('Ashley')
attendees.extent(['James', 'Guil'])
optional_invitees = ['Ben', 'Dave']
potential_attendees = attendees + optional_invitees
print('there are', len(potential_attendees), 'attendees currently') #8


#console
python -i meeting.py # interact with Python from REPL
for attendee in attendes: # set the attendee each time through the loop
    print (attendee)

   # attendee byitself will be set as the last item, here is 'Guil'
   # 'Ashley' in attendees - True
     
    
    
# wishlist.py

books = [
    "Learning Python: Powerful Object-Oriented Programming - Mark Lutz",
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinney",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
]

# print("suggested_gift: {}".format(books[0]))

# print("brooks: ")
# for book in books:
#     print("* " + book)
    
def display_wishlist(display_name, wishes):
    items = wishes.copy()   # make an unrelated copy of the "wishes" list, it is mutable
    print(display_name + ':')
    suggested_gift = items.pop(0)  # the pop command is changing the list "wishes", we change it to the copy file now
    print("=======>", suggested_gift, "<=======")
    for item in items:
        print("* " + item)
    print()
    
display_wishlist("Books", books)
display_wishlist("Video Games", video_games)
display_wishlist("Video Games", video_games)



# in Python console
python
inventory = ["shield", "apple", "sword", "bow", "boomerang"]
inventory.remove("apple")       # no more apple in the list

for item in inventory:
    inventory.remove(item)
inventory # ["sword", "boomerang"]

for item in inventory.copy():
    inventory.remove(item)
inventory # []



# exercise

for continent in continents: 
    if continent[0] == 'A':  #only print continents that begin with the letter "A"
        print("* " + continent)

    

all_restaurants = [
    "Taco City",
    "Burgertown",
    "Tacovilla",
    "Hotdog station",
    "House of tacos",
]

def tacos_only(restaurants):
    taco_joints = restaurants.copy()
    for taco_joint in taco_joints.copy():
        if "taco" not in taco_joint.lower():
            taco_joints.remove(taco_joint)
    return taco_joints

dinner_options = tacos_only(all_restaurants)

# Why do you think the author used the copy method in the for loop here:
    # modifying a list while looping through it is discouraged as it will produce unexpected result,
    # this code is looping through a copy and then modifying the original
    
    
    
turtles = [
    "Michelangelo",
    "Leonardo",
    "Raphael",
    "Donatello",
]

def shredder(names):
    if len(names) >= 1:
        names[0] = "Bebop"

shredder(turtles)

for turtle in turtles:
    print("* " + turtle)
    
#     What would the output be?
#     * Bebop
#     * Leonardo
#     * Raphael
#     * Donatello
    #Lists are mutable and that shredder method changed the list!
