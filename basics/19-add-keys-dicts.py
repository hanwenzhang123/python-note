To add a single key: value pair to a dictionary, we can use the syntax:

dictionary[key] = value

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

menu["cheesecake"] = 8

{"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2, "cheesecake": 8}


animals_in_zoo = {}
animals_in_zoo['zebras'] = 8
animals_in_zoo['monkeys'] = 12
animals_in_zoo['dinosaurs'] = 0
print(animals_in_zoo)


{'zebras': 8, 'monkeys': 12, 'dinosaurs': 0}


#Add Multiple Keys
#we can use the .update() method.


sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
{"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "guest room": 25, "patio": 34}


user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

{'teraCoder': 9018293, 'proProgrammer': 119238, 'theLooper': 138475, 'stringQueen': 85739}
