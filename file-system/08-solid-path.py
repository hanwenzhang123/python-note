import pathlib

def get_root():
  root = pathlib.PurePath(
    input("What is the full path where you would like the project?")
  )
  if not root.is_absolute():
    return get_root()
  return root

def main():
  project_root = get_root()
  project_name = None
  while not project_name:
    project_name = input("what is the full name for the project?").strip()
    print("creating {} in {}".format(project_name, project_root))
  
if __name__ == '__main__':
  main()
  
  
#solid path
  
#I'd like you to change how get_root works. 
#I still want to ask for a path but if the path is relative, change it into an absolute path. 
#You can assume that the path is relative from the current working directory. 
#The function should always return an absolute path.

import pathlib


def get_root():
    root = pathlib.PurePath(
        input("What's the full path where you'd like the project? ")
    )
    if not root.is_absolute():
        return get_root()
    return root
