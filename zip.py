# zip(*iterables) = aggregate elements from two or more iterables (lists, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

# Example: Two iterables

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@assword", "abc123", "guest")

# We want to zip elements from every pair to form a tuple (i.e ("Dude", "p@assword"))

users = zip(usernames, passwords)

for i in users:
    print(i)

# It is possible to cast/wrap the zip object in another type of iterable (i.e list, dictionary, etc.)

users = list(zip(usernames, passwords))

# A very useful function of this is to create (key,value) pairs in a dictionary

users = dict(zip(usernames, passwords))

for key,value in users.items():
    print(key + ": " + value)


# Example: Three iterables

# We will add another list 

login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

users = zip(usernames, passwords, login_date)

for i in users:
    print(i)

