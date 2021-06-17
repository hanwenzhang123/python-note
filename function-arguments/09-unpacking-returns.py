A Python function can return multiple things. 
This is especially useful in cases where bundling data into a different structure (a dictionary or a list, for instance) would be excessive. 
we can return multiple pieces of data by separating each variable with a comma:

def multiple_returns(cool_num1, cool_num2):
  sum_nums = cool_num1 + cool_num2
  div_nums = cool_num1 / cool_num2
  return sum_nums, div_nums



sum_and_div = multiple_returns(20, 10)
 
print(sum_and_div)
# Prints "(30, 2)"
 
print(sum_and_div[0])
# Prints "30"



sum, div = multiple_returns(18, 9)
 
print(sum)
# Prints "27"
 
print(div)
# Prints "2"



#script.py
def scream_and_whisper(text):
    scream = text.upper()
    whisper = text.lower()
    return scream, whisper

the_scream, the_whisper = scream_and_whisper("Hello There!")
