def insert_user_in_database(name, age):
    print(f"User inserted in DB for {name}, {age}")

# A function has to be called
insert_user_in_database("Alice", 34)

# Function returns (holds) value for later use
def insert_user_in_database(name, age):
    return f"User inserted in DB for {name}, {age}"

print(insert_user_in_database("Alice", 34))

# --- Customer 1 (Texas) ---
amount1 = 1000
state1 = "TX"
if state1 == "TX":
    tax_rate1 = 0.0625
elif state1 == "CA":
    tax_rate1 = 0.0725
else:
    tax_rate1 = 0.05
total_tax1 = amount1 * tax_rate1
print(f"Customer 1 Tax: ${total_tax1}")

# --- Customer 2 (California) ---
amount2 = 2500
state2 = "CA"
if state2 == "TX":
    tax_rate2 = 0.0625
elif state2 == "CA":
    tax_rate2 = 0.0725
else:
    tax_rate2 = 0.05
total_tax2 = amount2 * tax_rate2
print(f"Customer 2 Tax: ${total_tax2}")

# --- Customer 3 (Other) ---
amount3 = 500
state3 = "NY"
if state3 == "TX":
    tax_rate3 = 0.0625
elif state3 == "CA":
    tax_rate3 = 0.0725
else:
    tax_rate3 = 0.05
total_tax3 = amount3 * tax_rate3
print(f"Customer 3 Tax: ${total_tax3}")



# Function Way:

# Define the logic ONCE
def calculate_tax(amount, state):
    if state == "TX":
        tax_rate = 0.0625
    elif state == "CA":
        tax_rate = 0.0725
    else:
        tax_rate = 0.05
    return amount * tax_rate

# Reuse it 50 times with a single line of code
print(f"Customer 1 Tax: ${calculate_tax(1000, 'TX')}")
print(f"Customer 2 Tax: ${calculate_tax(2500, 'CA')}")
print(f"Customer 3 Tax: ${calculate_tax(500, 'NY')}")