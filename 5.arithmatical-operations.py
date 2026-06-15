# --- 1. Multiplication (*) ---
# You buy 3 pizzas. Each pizza costs $15.
pizza_count = 3
price_per_pizza = 15
total_pizza_cost = pizza_count * price_per_pizza
print(f"Total pizza cost: ${total_pizza_cost}")

# --- 2. Addition (+) ---
# You also add a bottle of soda for $4.
soda_cost = 4
total_bill = total_pizza_cost + soda_cost
print(f"Total bill with soda: ${total_bill}")

# --- 3. Subtraction (-) ---
# You have a discount coupon that saves you $5.
coupon = 5
final_bill = total_bill - coupon
print(f"Final bill after coupon: ${final_bill}")

# --- 4. Division (/) ---
# You split the final bill equally among 4 friends.
# Note: Standard division always returns a float (decimal number).
friends = 4
cost_per_person = final_bill / friends
print(f"Each person pays: ${cost_per_person}")

# --- 5. Floor Division (//) ---
# Each pizza has 8 slices. Total slices = 3 * 8 = 24.
# You want to know how many WHOLE slices each of the 5 people at the party can eat equally.
total_slices = 24
people_eating = 5
slices_per_person = total_slices // people_eating
print(f"Whole slices per person: {slices_per_person}")

# --- 6. Module / Mod (%) ---
# Find out how many leftover slices will remain in the box after everyone takes their equal share.
leftover_slices = total_slices % people_eating
print(f"Leftover slices left in the box: {leftover_slices}")  # Output: 4

# --- 7. Exponent / Power (**) ---
# A square pizza box is 12 inches by 12 inches. Find the area of the box base (12 squared).
box_side = 12
box_area = box_side ** 2
print(f"Area of the pizza box base: {box_area} square inches")  # Output: 144