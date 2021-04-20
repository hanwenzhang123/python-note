#reading files
open() - Opens a file in Python. This won't contain the content of the file, it just points to it in memory.
.read() - Reads the entire contents of the file object it's called on.
.close() - Closes the file object it's called on. This clears the file out of Python's memory.
r'string' - A raw string that makes writing regular expressions easier.
re.match(pattern, text, flags) - Tries to match a pattern against the beginning of the text.
re.search(pattern, text, flags) - Tries to match a pattern anywhere in the text. Returns the first match.
re.findall(pattern, text, flags) - Finds all non-overlapping occurrences of the pattern in the text.
.findall() gives us a list of results, not actual matches. We want .finditer() - gives us an iterable full of match objects

# A better way to read files
# If you don't know the size of a file, it's better to read it a chunk at a time and close it automatically. The following snippet does that:

# with open("some_file.txt") as open_file:
#     data = open_file.read()
    
# The with causes the file to automatically close once the action inside of it finishes. 
# And the action inside the .read(), will finish when there are no more bytes to read from the file.


#escape characters
\w - matches an Unicode word character. That's any letter, uppercase or lowercase, numbers, and the underscore character. In "new-releases-204", \w would match each of the letters in "new" and "releases" and the numbers 2, 0, and 4. It wouldn't match the hyphens.
\W - is the opposite to \w and matches anything that isn't an Unicode word character. In "new-releases-204", \W would only match the hyphens.
\s - matches whitespace, so spaces, tabs, newlines, etc.
\S - matches everything that isn't whitespace.
\d - is how we match any number from 0 to 9
\D - matches anything that isn't a number.
\b - matches word boundaries. What's a word boundary? It's the edges of word, defined by white space or the edges of the string.
\B - matches anything that isn't the edges of a word.
\A and \Z. These match the beginning and the end of the string, respectively. Though, ^ and $ are more commonly used and usually what you actually want.
r"\w" * 5 would create r"\w\w\w\w\w"


New terms
\w{3} - matches any three word characters in a row.
\w{,3} - matches 0, 1, 2, or 3 word characters in a row.
\w{3,} - matches 3 or more word characters in a row. There's no upper limit.
\w{3, 5} - matches 3, 4, or 5 word characters in a row.
\w? - matches 0 or 1 word characters.
\w* - matches 0 or more word characters. Since there is no upper limit, this is, effectively, infinite word characters.
\w+ - matches 1 or more word characters. Like *, it has no upper limit, but it has to occur at least once.


Sets
[abc] - this is a set of the characters 'a', 'b', and 'c'. It'll match any of those characters, in any order, but only once each.
[a-z], [A-Z], or [a-zA-Z] - ranges that'll match any/all letters in the English alphabet in lowercase, uppercase, or both upper and lowercases.
[0-9] - range that'll match any number from 0 to 9. You can change the ends to restrict the set.


Negation
[^abc] - a set that will not match, and, in fact, exclude, the letters 'a', 'b', and 'c'.


Group
([abc]) - creates a group that contains a set for the letters 'a', 'b', and 'c'. This could be later accessed from the Match object as .group(1)
(?P<name>[abc]) - creates a named group that contains a set for the letters 'a', 'b', and 'c'. This could later be accessed from the Match object as .group('name').
.groups() - method to show all of the groups on a Match object.
^ - specifies, in a pattern, the beginning of the string.
$ - specifies, in a pattern, the end of the string.
^~~~~$ beginning and the end of the string


re flag
re.IGNORECASE or re.I - does not care upper or lower case as a flag to make a search case-insensitive. re.match('A', 'apple', re.I) would find the 'a' in 'apple'.
re.VERBOSE or re.X - flag that allows regular expressions to span multiple lines and contain (ignored) whitespace and comments.
re.MULTILINE or re.M - flag to make a pattern regard lines in your text as the beginning or end of a string.


compiling and loops
re.compile(pattern, flags) - method to pre-compile and save a regular expression pattern, and any associated flags, for later use.
.groupdict() - method to generate a dictionary from a Match object's groups. The keys will be the group names. The values will be the results of the patterns in the group.
re.finditer() - method to generate an iterable from the non-overlapping matches of a regular expression. Very handy for for loops.
.group() - method to access the content of a group. 0 or none is the entire match. 1 through how ever many groups you have will get that group. Or use a group's name to get it if you're using named groups.



#address_book.py

import re   #library - regular expression

name_file = open('names.txt', encoding='utf-8')
data = name_file.read()
names_file.close()

last_name = r'Love'
first_name = r'Kenneth'
#print(re.match(last_name, data)) #match for the beginning of the string
#print(re.search(first_name, data)) #search for somewhere in the string
#print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data)) #? means the one before should show up 0 time or 1 time
#prirnt(re.findall(r'\w*, \w+', data)) # *universal, zero or infinite number of time
#print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
#print(re.findall(r'\b[trehous]{9}+\b', data, re.I)) #set of 9
# print(re.findall(r"""     #the email without gov
#     \b@[-\w\d.]*   #first a word boundary, an @, and then any number of characters
#     [^gov\t]+   # ignore 1+ instances of the letters, 'g', 'o', or 'v' and a tab.
#     \b          # match another word boundary
#     """, data, re.VERBOSE | re.I))
# print(re.findall(r"""
#     \b[-\w]+, # find a word boundary, 1+hyphens or characters, and a comma
#     \s        # find 1 whitespac
#     [-\w]+     # 1+ hypens and characteres and explicit spaces
#     [^\t\n]     #ignore tabs and new lines
#     """, data, re.X))
line = re, search(r'''
    ^(?P<name>[-\w ]+, \s[-\w ]+)\t      #last and first name
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t    #email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4}?\t  #phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?       #job and company
    (?P<twitter>@[\w\d]+)?$      #twitter
''', data, re.X|re.M))

print(line)
print(line.groupdict())


line = re, compile(r'''
    ^(?P<name>(?P<last>[-\w ]*), \s(?P<first>[-\w ]+))\t      #last and first name
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t        #email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4}?\t  #phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?       #job and company
    (?P<twitter>@[\w\d]+)?$      #twitter
''', re.X|re.M))        #don't need the data here

#print(line.search(data).groupdict())
for match in line.finditer(data):
    print('{first}{last}<{email}>'.format(**match.groupdict()))


    
