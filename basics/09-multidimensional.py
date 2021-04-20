travel_expenses = [
    [5.00, 2.75, 22.00, 0.00, 0.00],
    [24.75, 5.50, 15.00, 22.00, 8.00],
    [2.75, 5.50, 0.00, 29.00, 5.00],
]

print("Travel Expenses: ")
week_number = 1
for week in travel_expenses:
  print("* week #{}: ${}".format(week_number, sum(week)))
  week_number += 1


# console
lens(travel_expenses) # 3

travel_expenses[0]
# [5.00, 2.75, 22.00, 0.00, 0.00]

travel_expenses[0][1]
# 2.75


# exercise
bradys = [
    ["Marsha", "Carol", "Greg"],
    ["Jan", "Alice", "Peter"],
    ["Cindy", "Mike", "Bobby"],
]
# Which of the following options would return "Alice"?
# bradys[1][1]       # it is zero based 



# The first dimension is group, the second is group members.
# Loop through each group and output the members joined together with a ", " comma space as a separator
# Then print out see only groups that are trios, you know 3 members.

musical_groups = [
    ["Ad Rock", "MCA", "Mike D."],
    ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"],
    ["Salt", "Peppa", "Spinderella"],
    ["Rivers Cuomo", "Patrick Wilson", "Brian Bell", "Scott Shriner"],
    ["Chuck D.", "Flavor Flav", "Professor Griff", "Khari Winn", "DJ Lord"],
    ["Axl Rose", "Slash", "Duff McKagan", "Steven Adler"],
    ["Run", "DMC", "Jam Master Jay"],
]

for group in musical_groups:
    print(", ".join(group))
    break
for tri in musical_groups:
    if len(tri) == 3:
        print(", ".join(tri))
