positional argument unpacking, because it unpacks arguments given by position.

def shout_strings(*args):
  for argument in args:
    print(argument.upper())
 
shout_strings("hi", "what do we have here", "cool, thanks!")
# Prints out:
# "HI"
# "WHAT DO WE HAVE HERE"
# "COOL, THANKS!"


def truncate_sentences(length, *sentences):
  for sentence in sentences:
    print(sentence[:length])
 
truncate_sentences(8, "What's going on here", "Looks like we've been cut off")
# Prints out:
# "What's g"
# "Looks li"


from os.path import join

path_segment_1 = "/Home/User"
path_segment_2 = "Codecademy/videos"
path_segment_3 = "cat_videos/surprised_cat.mp4"

# join all three of the paths here!
print(join(path_segment_1, path_segment_2, path_segment_3))

def myjoin(*args):
  joined_string = args[0]
  for arg in args[1:]:
    joined_string += '/' + arg
  return joined_string

print(myjoin(path_segment_1, path_segment_2, path_segment_3))
  
