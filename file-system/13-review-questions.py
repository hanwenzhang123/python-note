What does `os.path.isabs()` tell us?
whether or not a path is absolute

When we used os.mkdir() and give it a path that already exists, it throws a FileExistsError.

What function should I use if I want to move one file or directory to a new location but the new location might not currently exist?
os.renames

When you delete a file or directory using os.rmdir or os.remove, where does the file or directory go?

When you use os.removedirs() to delete one or more directories, if the directory is *not* empty, what exception is thrown?

os.path.join() works just like str.join() and you do not need to provide the combining string, either a forward or backward slash.


When you're using pathlib.Path, you can use / to join pieces of a path.

I want to delete a directory. Finish this snippet:
os.("/grades/students.json")

What directory does .. represent?

Which of these is likely the root directory on a Windows machine?
F:\
