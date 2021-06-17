All named positional parameters
An unpacked positional parameter (*args)
All named keyword parameters
An unpacked keyword parameter (**kwargs)


def main(filename, *args, user_list=None, **kwargs):
  if user_list is None:
    user_list = []
 
  if '-a' in args:
    user_list = all_users()
 
  if kwargs.get('active'):
    user_list = [user for user_list if user.active]
 
  with open(filename) as user_file:
    user_file.write(user_list)
    
    
    
    A possible call to the function could look like this:

main("files/users/userslist.txt", 
     "-d", 
     "-a", 
     save_all_records=True, 
     user_list=current_users)
In the body of main() these arguments would look like this:

filename == "files/users/userslist.txt"
args == ('-d', '-a)
user_list == current_users
kwargs == {'save_all_records': True}
         
         
#script.py
def remove(filename, *args, **kwargs):
  with open(filename) as file_obj:
    text = file_obj.read()
  for arg in args:
    text = text.replace(arg, "")
  for kwarg, replacement in kwargs.items():
    text = text.replace(kwarg, replacement)
  return text

print(remove("text.txt", "generous", "gallant", fond="amused by", Robin="Mr. Robin"))
