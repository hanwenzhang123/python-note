functools.reduce() takes a function and an iterable. The function, though, takes two arguments. 
The first time it runs, the two arguments will be the first two items in the iterable. 
Every time after that, the first argument will be the result of the last time the function was run. 
The second argument will be the next value from the iterable. 
When the iterable is out of items, reduce() will return whatever the function returned last.

Think about adding up all of the numbers in a column. You add the top two, then add the third number to the sum you got from the first two. 
Then you add the fourth number to the sum of the top three, and so on.

Calling a function over again from within itself is known as recursion and it's what makes reduce() able to do its job.


