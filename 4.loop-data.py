# A list of product prices in dollars
dollar_prices = [1.50, 4.99, 10.00, 25.50]

# Create an empty list to store our results
cents_prices = []

# Loop through each price, multiply by 100, and add it to the new list
for price in dollar_prices:
    cents = int(price * 100)
    cents_prices.append(cents)

print(cents_prices)



# List Comprehension

dollar_prices = [1.50, 4.99, 10.00, 25.50]

# One single line replaces the 4 lines of code above
cents_prices = [int(price * 100) for price in dollar_prices]

print(cents_prices)
# Output: [150, 499, 1000, 2550]
