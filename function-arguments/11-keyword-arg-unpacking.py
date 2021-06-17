**kwargs gives us a dictionary with all the keyword arguments that were passed to arbitrary_keyword_args

def arbitrary_keyword_args(**kwargs):
  print(type(kwargs))
  print(kwargs)
  # See if there's an "anything_goes" keyword arg
  # and print it
  print(kwargs.get('anything_goes'))
 
arbitrary_keyword_args(this_arg="wowzers", anything_goes=101)
# Prints "<class 'dict'>
# Prints "{'this_arg': 'wowzers', 'anything_goes': 101}"
# Prints "101"


# Checkpoint 1
print("My name is {name} and I'm feeling {feeling}.".format(
	name="Tim",
  feeling="10/10",
))

# Checkpoint 2
from products import create_product

# Update create_products() to take arbitrary keyword arguments
def create_products(**products_dict):
  for name, price in products_dict.items():
    create_product(name, price)

# Checkpoint 3
# Update the call to `create_products()` to pass in this dictionary as a series of keyword
create_products(
  Baseball='3',
  Shirt='14',
  Guitar='70')


My name is Tim and I'm feeling 10/10.
Baseball created, being sold for $3
Shirt created, being sold for $14
Guitar created, being sold for $70
