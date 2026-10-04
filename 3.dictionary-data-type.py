# Creating the dictionary
employee_directory = {
    "EMP101": "Anis Rahman",
    "EMP102": "Sultana Kamal",
    "EMP103": "Tamim Iqbal"
}

# 1. Looking up a value (Fast Search)
print(employee_directory["EMP102"])  


# 2. Adding a new employee
employee_directory["EMP104"] = "Sakib Al Hasan"

# 3. Overwriting/Updating an existing key
employee_directory["EMP101"] = "Khalilur Hasan" 

print(employee_directory)