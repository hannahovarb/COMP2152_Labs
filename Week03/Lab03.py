# start_python_file.py
# Lab 03 – Python Collections Practice
# Covers: Lists, Tuples, Sets, Dictionaries

# ============================================================
# Question 1: Student Grades List
# ============================================================
print("=" * 50)
print("Question 1: Student Grades List")
print("=" * 50)
# 1. Create a list called grades with these initial values: [85, 92, 78, 95, 88]
grades = [85, 92, 78, 95, 88]

# 2. Use append() to add a new grade of 90 to the list
grades.append(90)

# 3. Use sort() to sort the grades in ascending order
grades.sort()

# 4. Print the sorted list
print("Sorted grades:", grades)

# 5. Print the highest grade (last element using negative indexing)
print("Highest grade:", grades[-1])

# 6. Print the lowest grade (first element)
print("Lowest grade:", grades[0])

# 7. Print the total number of grades using len()
print("Total number of grades:", len(grades))

print()

# ============================================================
# Question 2: Shopping Cart
# ============================================================
print("=" * 50)
print("Question 2: Shopping Cart")
print("=" * 50)
# 1. Create a list called cart with these items: ["apple", "banana", "milk", "bread", "apple", "eggs"]
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]

# 2. Use count() to find how many times "apple" appears in the cart
print("Number of apples:", cart.count("apple"))

# 3. Use index() to find the position of "milk" in the cart
print("Position of milk:", cart.index("milk"))

# 4. Use remove() to remove one "apple" from the cart
cart.remove("apple")

# 5. Use pop() to remove and print the last item from the cart
print("Removed item using pop:", cart.pop())

# 6. Check if "banana" is in the cart and print the result
print("Is banana in cart?", "banana" in cart)

# 7. Print the final cart
print("Final cart:", cart)
print()

# ============================================================
# Question 3: Coordinate System (Tuples)
# ============================================================
print("=" * 50)
print("Question 3: Coordinate System")
print("=" * 50)
# 1. Create a tuple called point1 with values (3, 5)
point1 = (3, 5)

# 2. Create a tuple called point2 with values (7, 2)
point2 = (7, 2)

# Print points
print("Point 1:", point1)
print("Point 2:", point2)

# 3. Unpack point1 into variables x1 and y1
x1, y1 = point1

# 4. Unpack point2 into variables x2 and y2
x2, y2 = point2

print(f"x1 = {x1}, y1 = {y1}")
print(f"x2 = {x2}, y2 = {y2}")

# 5. Calculate the distance between points using the given formula
distance = ((x2 - x1) * x2 + (y2 - y1) * x2) * 0.5
print("Distance between points:", distance)

# 6. Create a tuple from the string "PYTHON" using the tuple() constructor
characters_tuple = tuple("PYTHON")
print("Characters tuple:", characters_tuple)

# 7. Print each character from the tuple using a for loop
print("Python")
for char in characters_tuple:
    print(char)

print("-" * 40)
print()

# ============================================================
# Question 4: Class Attendance (Sets)
# ============================================================
print("=" * 50)
print("Question 4: Class Attendance")
print("=" * 50)
# 1. Create a set called monday_class with students
monday_class = {"Alice", "Bob", "Charlie", "Diana"}

# 2. Create a set called wednesday_class with students
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

# 3. Use add() to add "Grace" to monday_class
monday_class.add("Grace")

# Print initial sets
print("Monday class:", monday_class)
print("Wednesday class:", wednesday_class)

# 4. Find students who attended both classes using intersection (&)
both_classes = monday_class & wednesday_class
print("Attended both classes:", both_classes)

# 5. Find students who attended either class using union
either_class = monday_class | wednesday_class
print("Attended either class:", either_class)

# 6. Find students who attended only Monday using difference (-)
only_monday = monday_class - wednesday_class
print("Only Monday:", only_monday)

# 7. Find students who attended only one class (not both) using symmetric difference (^)
only_one_class = monday_class ^ wednesday_class
print("Only one class (not both):", only_one_class)

# 8. Check if monday_class is a subset of the union using <=
is_subset = monday_class <= either_class
print("Is Monday subset of all students?", is_subset)
print()

# ============================================================
# Question 5: Contact Book (Dictionaries)
# ============================================================
print("=" * 50)
print("Question 5: Contact Book")
print("=" * 50)
# 1. Create a dictionary called contacts
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

# 2. Print Alice's phone number by accessing the dictionary
print("Alice's number:", contacts["Alice"])

# 3. Add a new contact: "Diana" with number "555-4321"
contacts["Diana"] = "555-4321"
print("Contacts after adding Diana:", contacts)

# 4. Update Bob's number to "555-0000"
contacts["Bob"] = "555-0000"
print("Contacts after updating Bob:", contacts)

# 5. Delete Charlie's contact using del
del contacts["Charlie"]
print("Contacts after deleting Charlie:", contacts)

# 6. Print all contact names using keys()
print("All names:", contacts.keys())

# 7. Print all phone numbers using values()
print("All numbers:", contacts.values())

# 8. Print the total number of contacts
print("Total contacts:", len(contacts))

print()