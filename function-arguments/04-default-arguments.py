a standard function definition that defines two parameters requires two arguments passed into the function.

# Function definition with two required parameters
def create_user(username, is_admin):
  create_email(username)
  set_permissions(is_admin)
 
# Function call with all two required arguments
user1 = create_user('johnny_thunder', True)
 
# Raises a "TypeError: Missing 1 required positional argument"
user2 = create_user('djohansen')
