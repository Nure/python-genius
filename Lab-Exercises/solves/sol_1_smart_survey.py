name = str(input("What is your name?"))
while name == "":
    name = str(input("Please enter your name: "))

age = int(input("How old are you? "))
while age < 10 and age > 120:
    if age > 0 and age < 10:
        print("Sorry, you are too young to participate in this survey.")
        exit()
    elif age > 120:
        print("Sorry, you have entered an invalid age.")
    age = int(input("Please enter a valid age: "))

dev_status = bool(input("Are you a developer? (True/False) "))
while dev_status not in [True, False]:
    dev_status = bool(input("Please enter True or False: "))

roles = {
    "Tier 1": "Admin",
    "Tier 2": "Standard Executive Access",
    "Tier 3": "Guest"
}

if age < 18:
    print(f"Hello {name}, you are a {roles['Tier 3']} with limited access.")
elif dev_status:
    print(f"Hello {name}, you are a {roles['Tier 1']} with full access.")
else:
    print(f"Hello {name}, you are a {roles['Tier 2']} with standard access.")
