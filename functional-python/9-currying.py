Currying - technique is used to create alternate versions of a function based on the number of provided arguments
Currying may actually change the behavior of the function, not just its arguments.

you can call a func and that func if does not have enough argument
it will fill in as many argument as it can to itself and sen you back a new version of itself iwth those arguments already filled in, and you can put in new ones after that

def curried_f(x, y=None, z=Zone):
 def f(x, y, z):
  return x**3 + y**2 + z
 
  if y is not None and z is not None:
    return f(x, y, z)
  if y is not None:
    return lambda z: f(x, y, z)
   
   return lambda y, z=None: (
    f(x, y, z) if (y is not None and z is not None)
    else (lambda z: f(x, y, z)))
  
print(curried_f(2, 3, 4)) #21
g = curried_f(2)
print(g)
h = g(3)
print(h)
i = h(4)
print(i)
 
