# reduce() works differently than map() and filter() . It does not return a new list based on the function and iterable we've passed. Instead, it returns a single value. Also, in Python 3 reduce() isn't a built-in function anymore, and it can be found in the functools module. Map takes all objects in a list and allows you to apply a function to it whereas Filter takes all objects in a list and runs that through a function to create a new list with all objects that return True in that function.