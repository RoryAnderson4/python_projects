Bill = float(input('Enter bill amount (£): '))

vat_tax = Bill * 0.20

total = Bill + vat_tax

print(f'VAT Tax (20%): £{vat_tax: .2f}')
print(f'Total Bill to charge: £{total: .2f}')
