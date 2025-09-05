"""
Lesson: Lists and Dictionaries in Python
----------------------------------------
This file is intentionally incomplete.
Your job is to experiment, fill in blanks, and notice how lists and dictionaries store and organize data.
"""

# --- Section 1: Making a List ---

# Lists keep items in order.
# Example: foods = ["pizza", "sushi", "ice cream"]

# TODO: Create a list of 5 of your favorite foods.

foods = ["burgers", "chicken", "eggs", "potatos", "steak"]

# Access items by index (first = 0):
print(f"The first food is {foods[0]}")
print(f"The last food is {foods[-1]}")

# Bug Exploration:
# Try printing foods[100] below.
# Q: What error do you get, and what does it mean?

# --- Section 2: Changing a List ---

# Lists can grow and shrink using built-in methods.

# TODO: Add a new food to the end of your list with .append()
foods.append("fries")

# TODO: Insert a food at the beginning with .insert()
foods.insert(0, "salad")

# TODO: Remove one food from the list with .remove()
foods.remove("eggs")

# TODO: How many foods are in the list? Use len()
length_of_foods = len(foods)
print(f"There are {length_of_foods} foods in the list.")

# Bug Exploration:
# Try removing something that isn’t in the list:
# foods.remove("chocolate")
# Q: What happens? Why?


# --- Section 3: Loops with Lists ---

# TODO: Write a for loop that prints each food in your list one by one.


# Bug Exploration:
# Change your loop to go past the length of the list:
for i in range(length_of_foods):
    print(f"Index {i} → {foods[i]}")
# Q: Why does this cause an error?


# --- Section 4: Dictionaries (Key–Value Pairs) ---

# Dictionaries let us label data with keys.
# Example: 
me = {
    "name": "Ethan",
    "age": 17,
    "student": True
    }

# TODO: Make a dictionary with at least 3 pieces of information about yourself.


# Access values using keys by using the .get() method rather than indexing
# print(f"My name is {me['name']}")
# print(f"My age is {me['age']}")
# print(f"My favorite color is {me['favorite_color']}")
name = me.get("name")
age = me.get("age")
student = me.get("student")
if student == True:
    student = "Yes"
else:
    student = "No"
print(f"My name is {name}")
print(f"My age is {age}")
print(f"Am I a student? {student}")
# Bug Exploration:
# Try printing a key that doesn’t exist.
# print(me["hometown"])
# Q: What kind of error is this? How could you check if a key exists before using it? Why is the .get() method useful here?


# --- Section 5: Changing a Dictionary ---

# TODO: Add a new key-value pair.
me["hobby"] = "coding"

# TODO: Change the value of an existing key.
me["age"] = 18

# TODO: Remove one key-value pair.
me.pop("student")

# Bug Exploration:
# Try removing a key that doesn’t exist:
# me.pop("grade")
# Q: What happens? Is this similar to removing from a list?


# --- Section 6: Loops with Dictionaries ---

# TODO: Write a loop that prints both the keys and values in your dictionary using .items()
number = 1
for number in range(len(me)):
    for key, value in me.items():
        print(f"{key} → {value}")
    number += 1

# Bug Exploration:
# What happens if you loop over just the dictionary without calling .items()?
# for key in me:
#     print(key)

# Q: Why does it only print the keys? How can you change your for loop to print key and value pairs?


# --- Section 7: Mixing Lists and Dictionaries ---

# TODO: Create a list of dictionaries. 
# Example: a list of 3 friends, where each friend has a name and favorite food.
friends = [
    {"name": "Alice", "favorite_food": "pizza"},
    {"name": "Bob", "favorite_food": "sushi"},
    {"name": "Charlie", "favorite_food": "ice cream"}
]

# TODO: Print the favorite food of the second friend.
print(f"The favorite food of the second friend is {friends[1]['favorite_food']}.")

# TODO: Loop through and print "<name> likes <food>" for each friend.
while True:
    for friend in friends:
        name = friend.get("name")
        favorite_food = friend.get("favorite_food")
        print(f"{name} likes {favorite_food}.")
    break

# Bug Exploration:
# What happens if you try to access friend["hobby"] when "hobby" doesn’t exist in the dictionary?
# Q: How might you prevent this kind of error in real programs?


# --- Section 8: Reflection ---
# Answer in comments:
# 1. How is a list different from a dictionary?
# 2. When would you want to use a dictionary instead of a list?
# 3. Can you think of a real-world situation where combining lists and dictionaries would be useful?
# 4. What types of mistakes gave you the most errors today?
# 5. How might noticing errors actually help you learn?