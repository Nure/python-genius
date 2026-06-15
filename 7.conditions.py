# When people talk about a "condition data type" in Python, they are referring to the Boolean (bool) data type.

# Booleans represent the core of all computer logic. A Boolean variable can only ever hold one of two possible values: True or False.

# We use Booleans to control the flow of our programs using conditional statements (like if, elif, and else).


# 1. How Booleans are Created
# Booleans are typically generated in two ways: by direct assignment or by using comparison operators.

# A. Comparison Operators Cheat Sheet
# When you compare two values, Python evaluates the expression and returns a Boolean (True or False).




# General Example: Human Survey Eligibility
# Imagine a survey script that checks if a person is legally an adult or if they qualify for a family tax credit.


# Raw Data
age = 34
has_kids = True

# 1. Evaluate conditional expressions (creates Boolean data)
is_adult = age >= 18       # Evaluates to True
qualifies_for_credit = (age > 30) and has_kids  # Evaluates to True

# 2. Use the Boolean data to control program flow
if is_adult:
    print("Survey access granted.")
else:
    print("Access denied: Must be 18 or older.")




# Here is a simple, practical example using if, elif, and else based on our human survey scenario.

# Imagine you are building an automated system that looks at a person's age and determines their movie ticket pricing category.

# Change this number to test different paths!
age = 25 

if age < 4:
    # This runs if age is less than 4
    print("Ticket is free for toddlers!")

elif age <= 12:
    # This runs if the first condition failed, but age is 12 or under
    print("Child ticket price: $8.00")

elif age < 65:
    # This runs if all previous conditions failed, but age is under 65
    print("Adult ticket price: $15.00")

else:
    # This runs as a fallback if absolutely everything else failed
    print("Senior citizen ticket price: $10.00")

