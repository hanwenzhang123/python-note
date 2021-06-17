How do you define a variable that you can’t assign a value to yet? You use None.
None is unique (there can’t be two different Nones) and immutable (you can’t update None or assign new attributes to it).


none_var = None
if none_var:
  print("Hello!")
else:
  print("Goodbye")  # Prints "Goodbye"



None is falsy, meaning that it evaluates to False in an if statement, which is why the above code prints “Goodbye”. 
None is also unique, which means that you can test if something is None using the is keyword.


# first we define session_id as None
session_id = None
 
if session_id is None:
  print("session ID is None!")
  # this prints out "session ID is None!"
 
# we can assign something to session_id
if active_session:
  session_id = active_session.id
 
# but if there's no active_session, we don't send sensitive data
if session_id is not None:
  send_sensitive_data(session_id)
  
  
  
  #script.py
from review_lib import get_next_review, submit_review

review = get_next_review()
if review is not None:
  submit_review(review)
   
