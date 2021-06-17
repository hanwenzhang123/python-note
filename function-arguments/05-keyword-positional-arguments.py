The required parameters need to occur before any parameters with a default argument.

# Raises a TypeError
def create_user(is_admin=False, username, password):
  create_email(username, password)
  set_permissions(is_admin)
  
In the above code, we attempt to define a default argument for is_admin without defining default arguments for the later parameters: username and password.
  
  
  
If we want to give is_admin a default argument, we need to list it last in our function definition:

# Works perfectly
def create_user(username, password, is_admin=False):
  create_email(username, password)
  set_permissions(is_admin)
  
  
  
#define a parameter with a default argument before a required parameter.
  import reqs as requests
from bs4 import BeautifulSoup

def get_id(html_id, website="http://coolsite.com"):
  request = requests.get(website)
  parsed_html = BeautifulSoup(website.content, features="html.parser")
  return parsed_html.find(id_=html_id)
