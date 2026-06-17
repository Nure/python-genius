 #  Lab 1: The Smart Survey Onboarding Engine
  print("Onboarding System Portal")
  name = input("Enter Your Full Name: ")
  age = int(input("Enter Your Age: "))
  is_devloper = input("Developer? (yes/no): ").lower() == "yes"

  if age < 18:
      tier = "Tier 3: Guest"
  elif is_devloper:  # age >= 18 এবং developer হলে
      tier = "Tier 1: Admin Infrastructure Access"
  else:         # age >= 18 কিন্তু developer না হলে
      tier = "Tier 2: Standard Executive Access"


  print(f"""
  ===================================
        PROFILE CONFIG CARD
  ===================================
  User Name    : {name}
  Verified Age : {age}
  Developer    : {'Yes' if is_devloper else 'No'}
  Access Level : {tier}
  ===================================
  """)

