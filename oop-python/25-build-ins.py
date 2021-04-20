# yield woks very similar to return but it does not immediately end the execution of the method like return does
# yield lets us send values back out of the function or the method as they are available and keep on working

class Inventory:
  def __init__(self):
    self.slots = []
    
  def add(self, item):
    self.slots.append(item)
    
  def __len__(self):
    return len(self.slots)
    
  def __contains__(self, item):
    return item in self.slots
    
  def __iter__(self):
      yield from self.slots  # same as the loop 'for item in self.slots: yield item'


#reversestr.py
  class ReverseStr(str):
    def __new__(*args, **kwargs):   # new for immutable objects
      self = str.__new__(*args, **kwargs)
      self = self [::-1] # reversed
      return self
    
#filledlist.py
import copy

class FilledList(list): #subclass, extends list
  def __list__(self, count, value, *args, **kwargs):
    super().__init__() # super().__init__() does not take any arguments
    for _ in range (count): # _ ignore the value
      self.append(copy.copy(value)) #copy.copy a new object is created, given a new id, then the new id is appended.
      
#javascriptobject.py
class JavaScriptObject(dict): #subclass, extends dict
  def __getattribute__(self, item):
    try:
      return self[item]
    except KeyError:
      return super().__getattribute__(item)
    
# Super() isn't just necessarily used to inherit methods from a parent class 
# but to override methods that the parent class has assigned, it also inherits certain methods and overrides others that it wants to change



# exercise    

  class Album:
    def __init__(self):
        self.songs = []
    def add(self, song):
        self.songs.append(song)
    def __iter__(self):
        yield from self.songs  #yield from so the songs in our album can be iterated through
      
      
class Double(int):
    def __new__(*args, **kwargs):
        self = int.__new__(*args,**kwargs)  # override __new__. Create a new int instance from whatever is passed in as arguments and keyword arguments.
        self *=   2
        return self

print(Double(5)) 
      
    
# Override the __len__ method so that it always returns the wrong number of items in the list.
class Liar(list):
    def __len__(self):
        return super().__len__() + 1
      
      
