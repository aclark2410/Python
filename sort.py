# sort() method = used with lists

# sort() function = used with iterables

students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]

students.sort()

for i in students:
    print(i)

# We can reverse the order by typing in the sort() argument reverse=True

students.sort(reverse=True)

for i in students:
    print(i)


# To use the sort() function we pass in the iterable as an argument, the second argument can be used to reverse the order

sorted_students = sorted(students, reverse=False)

for i in sorted_students:
    print(i)

print()

# In this example we can sort a list of tuples by one of the items in the list

students_tuple = [("Squidward", "F", 60),
                  ("Sandy", "A", 33),
                  ("Patrick", "D", 36),
                  ("Spongebob", "B", 20),
                  ("Mr. Krabs", "C", 78)]


# If we used the same sort() method, it would sort by the first column
# We want to use the keyword argument and pass in an object.
# We can use the lambda function and pass in the column index we want to sort by

grade = lambda grades: grades[1]

students_tuple.sort(key=grade)

for i in students_tuple:
    print(i)

print()


# To show this for the numeric value we can set the index of the grade in the lambda function to 2

age = lambda ages: ages[2]

students_tuple.sort(key=age)

for i in students_tuple:
    print(i)

print()

# Remember we can always use reverse = True/False on this method too! 

age = lambda ages: ages[2]

students_tuple.sort(key=age, reverse=True)

for i in students_tuple:
    print(i)