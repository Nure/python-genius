# Lab 1: The Smart Survey Onboarding Engine

# 1. Capture inputs from user (Name, Age, Developer Status)
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Cast to int for numeric comparison
is_developer = input("Are you a developer? (yes/no): ").strip().lower() == "yes"

# 2. Evaluate conditional logic to determine the clearance tier
if age < 18:
    tier = "Tier 3: Guest"
elif is_developer:
    tier = "Tier 1: Admin Infrastructure Access"
else:
    tier = "Tier 2: Standard Executive Access"

# 3. Print out the final profile card using an f-string
print(f"\n--- Profile Configuration Summary ---")
print(f"Name:      {name}")
print(f"Age:       {age}")
print(f"Developer: {'Yes' if is_developer else 'No'}")
print(f"Clearance: {tier}")
