# Setup our base variables
movie_ticket_price = 12
minimum_age = 18

customer_age = 20
customer_cash = 12

# --- 1. Greater Than (>) ---
# Is the customer older than the minimum age?
print(customer_age > minimum_age) 

# --- 2. Less Than (<) ---
# Is the ticket price less than the cash they have?
print(movie_ticket_price < customer_cash) 

# --- 3. Equal To (==) ---
# Does their cash exactly equal the ticket price?
# Note: We use TWO equals signs (==) to compare. A single (=) is for assigning variables.
print(customer_cash == movie_ticket_price) 

# --- 4. Not Equal To (!=) ---
# Is the customer's age different from the minimum age requirement?
print(customer_age != minimum_age)   

# --- 5. Greater Than or Equal To (>=) ---
# Can the customer pay for the ticket? (Do they have enough or exact cash?)
print(customer_cash >= movie_ticket_price) 

# --- 6. Less Than or Equal To (<=) ---
# Is the customer a minor? (Age 17 or younger)
print(customer_age <= 17)             