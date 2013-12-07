# The Standard Library and Object Orientation


# So, we now know how to use the basic language features of Python to write larger pieces of functionality

# Many of these pieces are required by programmers often, so are "bundled" with Python in what is called the *Standard Library*

# For example, there is a "random" module: http://docs.python.org/3.3/library/random.html?highlight=random#random

# We can use this in our project as follows:

import random

# Now that it is imported, we may access the functions contained within the random module:

my_random_number = random.choice([1,4,9,16])
print("My random number is: ", my_random_number)

# 1) Use the range() function we used earlier to choose a random student from a class of 150 students.

# 2) Looking at the web documentation for random, randomly (and uniformly) resort these students:

some_students = ['Alice', 'Bob', 'Charlotte', 'Dave']

# 3) Looking here: http://docs.python.org/3.0/library/urllib.request.html#examples, download the beneills.com homepage
#      and determine the most frequent word in the HTML source.  (search 'python word frequency' on Google)




# Now, I'll show you a class - the most important structure in *Object-Oriented Programming*

class Person:
    # height in metres, weight in kg
    def __init__(self, firstname, secondname, height, weight):
        self.firstname = firstname
        self.secondname = secondname
        self.height = height
        self.weight = weight

    def full_name(self):
        return self.firstname + " " + self.secondname
            
    def bmi(self):
        w = self.weight
        h = self.height
        return w/(h**2)

ben = Person("Ben", "Eills", 1.829, 73)

print(ben.full_name())
print(ben.bmi())


# 4) Create an instance of Person: Alice, a 1.6m, 100kg female with last name "House".

# 5) Add a *method* to the Person class that reports which weight category the person falls into.

