print('--- item tracker ---')

number_of_items = float(input('Enter number of items: '))
cost = float(input('enter cost of item (£): '))

total = number_of_items * cost

if number_of_items >= 50:
    print('bluk discount applied! (10% off)')
    total = total * 0.90

print(f"all together cost: £{total: .2f}")