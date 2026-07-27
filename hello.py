# A simple profit/budget calculator
print("--- Daily Business Profit Tracker ---")

# 1. Get input from the user
revenue = float(input("Enter today's total sales (£): "))
costs = float(input("Enter today's expenses (£): "))

# 2. Do the math
profit = revenue - costs

# 3. Show the result
print("-------------------------------------")
print(f"Total Profit Today: £{profit}")

if profit > 0:
    print("suficaint profit made! sick one gadj")
elif profit == 0:
    print("You broke even today.")
else:
    print("Warning: You ran at a loss today. ⚠️")