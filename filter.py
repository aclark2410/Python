# filter() = creates a collection of elements from an iterable for which a function for which a function returns True

# filter(function, iterable)

friends = [("Rachel", 19),
           ("Monica",18),
           ("Phoebe", 17),
           ("Joey", 16),
           ("Chandler", 21),
           ("Ross", 20)]


# Let's create a separate list for the friends who can go out drinking (i.e over 18 years old)

# First create a function that will return all of the entries of the desired index for the condition of being 18 or older

age = lambda data: data[1] >= 18

# We then map the function to the iterable and wrap the filter in a list to return another list

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)