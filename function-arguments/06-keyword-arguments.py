# Define a function with a bunch of default arguments
def log_message(logging_style="shout", message="", font="Times", date=None):
  if logging_style == 'shout':
    # capitalize the message
    message = message.upper()
  print(message, date)
 
# Now call the function with keyword arguments
log_message(message="Hello from the past", date="November 20, 1693")



#script.py
import shapes

def draw_shape(shape_name="box", character="x", line_breaks=True):
  shape = shapes.draw_shape(shape_name, character)
  if not line_breaks:
    print(shape[1:-1])
  else:
    print(shape)

# call draw_shape() with keyword arguments here:
draw_shape(character='m', line_breaks=False)

mmm
m m
mmm
