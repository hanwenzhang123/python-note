>>> import os
>>> import temfile
>>> with temfile.TemporaryDirectory() as tmpdirname:
...  print("Created temporary directory named{}".format(tmdirname))
...  with open(os.path.join(tmpdirname, 'temp_file.txt'), 'w') as f:
...    f.write('hello\n')
...  input()


>>> import os
>>> import temfile
>>> with temfile.TemporaryDirectory() as tmpfile:
...  tempfile.write(b'hello\n')
...  tempfile.seek(0)
...  tempfile.read()
  
fp = tempfile.TemporaryFile()
fp.write(b'hello\n')  #6
fp.close()

fp = tempfile.NamedTemporaryFile()
fp.name
