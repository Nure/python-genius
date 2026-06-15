name= input("what is your name ?")
age= int(input("what is your age?"))
developer= input("are you a developer?(yes/no)")

group1 = 'tier 3 : Guest'
group2 = 'tier 2: Standard Executive Access'
group3 = 'Tier 1: Admin Infrastructure Access'

if age < 18:
    print(group1)
elif age >= 18 and developer == 'yes':
    print(group3)
elif developer == 'no':
    print(group2) 
    