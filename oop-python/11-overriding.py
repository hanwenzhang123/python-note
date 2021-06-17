override a method definition is to offer a new definition for the method in our subclass.


class User:
  def __init__(self, username, permissions):
    self.username = username
    self.permissions = permissions
 
  def has_permission_for(self, key):
    if self.permissions.get(key):
      return True
    else:
      return False
    
    
class Admin(User):
  def has_permission_for(self, key):
    return True
  
  
  # Here we define an Admin class that subclasses User. 
  # It has all methods, attributes, and functionality that User has.
  
  
  
  # Create an Admin class that subclasses the User class.
  # Override User‘s .edit_message() method in Admin so that an Admin can edit any messages.
  class Message:
  def __init__(self, sender, recipient, text):
    self.sender = sender
    self.recipient = recipient
    self.text = text

class User:
  def __init__(self, username):
    self.username = username
    
  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text
      
class Admin(User):
  def edit_message(self, message, new_text):
    message.text = new_text
    
      
