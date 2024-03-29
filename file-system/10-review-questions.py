What does `os.path.isabs()` tell us?
whether or not a path is absolute

What function should I use if I want to move one file or directory to a new location but the new location might not currently exist?
os.renames

When you delete a file or directory using os.rmdir or os.remove, where does the file or directory go?
It is immediately deleted

When you use os.removedirs() to delete one or more directories, if the directory is *not* empty, what exception is thrown?
OSError

I want to delete a directory. Finish this snippet:
os.rmdir("/grades/students.json")

What directory does .. represent?
The directory above the current one

Which of these is likely the root directory on a Windows machine?
F:\

os.path.join() works just like str.join() and you do not need to provide the combining string, either a forward or backward slash.

When you're using pathlib.Path, you can use / to join pieces of a path.

When we used os.mkdir() and give it a path that already exists, it throws a FileExistsError.



  I want to change a file's filename. Which method should I use?
  os.rename
  
  Which method should you use if you need to create a path but one or more directories in it might not already exist?
  os.makedirs
  
  When using os.makedirs, an error is thrown if the desired directory already exists. How do you prevent that?
  exist_ok=True
  
  
  I'm using a temporary directory inside of a function. At what point would the directory, and any contents it may have, be deleted?
  When the function is finished
  
  
 When you delete a file with os.remove, that file is not placed in the system trash.

 You are not guaranteed to have a visible (in the file system) file when using tempfile. TemporaryFile
