# List Comprehensions = a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if/else for item in iterable]

# Example 1) list = [expression for item in iterable]

# Here is a simple program that squares the numbers in a list

squares = []

for i in range(1,11):
    squares.append(i*i)
print(squares)

# We can write this more efficiently in the form: list = [expression for item in iterable]

squares_1 = [i*i for i in range(1,11)]

print(squares_1)


# Example 2) list = [expression for item in iterable if conditional]

students = [100,90,80,70,60,50,40,30]

passing_grade = lambda x: x >= 60

passing_students = list(filter(passing_grade, students))

print(passing_students)

# we can write this more efficiently using conditional form: list = [expression for item in iterable if conditional]

passed_students_1 = [i for i in students if i >= 60]

print(passed_students_1)

# Example 3) list = [expression if/else for item in iterable]

# If we wanted to include an expression/result for the students who failed we can do so using if/else conditional]

passed_students_3 = [i if i >= 60 else "FAILED" for i in students]

print(passed_students_3)




