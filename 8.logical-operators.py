# and, or


not_married = True
age = 20

# For 'and' Both conditions/sides must be True
if not_married == True and age >= 18:
    print("Most elligible bachelor getting married")
else:
    print("Papa will....")


# For 'or' operator only requires at least one condition to be True. It will only return False if every single condition fails.
has_job = True
age = 20
if has_job == True or age >= 18:
    print("Most elligible bachelor getting married")
else:
    print("Okormar dheki, bia korte asche, maira...")