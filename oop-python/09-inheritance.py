# if we need a class that looks a lot like a class we already have

#1 
class User:
  is_admin = False
  def __init__(self, username)
    self.username = username
 
class Admin(User):
  is_admin = True
  
#2
lass Bin:
  pass

class RecyclingBin(Bin):
  pass
  
