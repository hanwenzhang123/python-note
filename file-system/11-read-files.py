#Reading a File
with open('real_cool_document.txt') as cool_doc:
  cool_contents = cool_doc.read()
print(cool_contents)


#Iterating Through Lines
with open('keats_sonnet.txt') as keats_sonnet:
  for line in keats_sonnet.readlines():
    print(line)
    

#Reading a Line
with open('millay_sonnet.txt') as sonnet_doc:
  first_line = sonnet_doc.readline()
  second_line = sonnet_doc.readline()
  print(second_line)
  
  
#Writing a File
with open('generated_file.txt', 'w') as gen_file:
  gen_file.write("What an incredible file!")
  
with open('bad_bands.txt', 'w') as bad_bands_doc:
  bad_bands_doc.write('The Beatles')

  
#Appending to a File
with open('generated_file.txt', 'a') as gen_file:
  gen_file.write("... and it still is")
  
with open('cool_dogs.txt', 'a') as cool_dogs_file:
  cool_dogs_file.write('Air Buddy')
  
#2
fun_cities_file = open('fun_cities.txt', 'a')
 
# We can now append a line to "fun_cities".
fun_cities_file.write("Montréal")
 
# But we need to remember to close the file
fun_cities_file.close()

#3
with open('fun_file.txt') as close_this_file:

  setup = close_this_file.readline()
  punchline = close_this_file.readline()

  print(setup)

  
#CVS file
with open('fun_file.txt') as close_this_file:

  setup = close_this_file.readline()
  punchline = close_this_file.readline()

  print(setup)
  

#Reading a CSV File
import csv

with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row['Cool Fact'])
  
  #2
import csv

with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = [book['ISBN'] for book in books_reader]
  
  
#Writing a CSV File
big_list = [{'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False}, {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False}, {'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False}, {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}] 
 
import csv
 
with open('output.csv', 'w') as output_csv:
  fields = ['name', 'userid', 'is_admin']
  output_writer = csv.DictWriter(output_csv, fieldnames=fields)
 
  output_writer.writeheader()
  for item in big_list:
    output_writer.writerow(item)
    
    
#Reading a JSON File
import json
 
with open('purchase_14781239.json') as purchase_json:
  purchase_data = json.load(purchase_json)
 
print(purchase_data['user'])
# Prints 'ellen_greg'


#2
import json

with open('message.json') as message_json:
  message = json.load(message_json)
  print(message['text'])
  
  
#Writing a JSON File
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json

with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)
 
