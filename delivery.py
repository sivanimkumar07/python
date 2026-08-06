import random
rice = 45
sugar = 40
oil = 130

rice_qty = 3
sugar_qty = 2.5
oil_qty = 1.8

rice_total = rice * rice_qty
sugar_total = sugar * sugar_qty
oil_total = oil * oil_qty

print("rice total:",rice_total)
print("sugar total:",sugar_total)
print("oil total:",oil_total)

total_bill = rice_total + sugar_total + oil_total
print("Total Bill: ₹", total_bill)

bill_int = int(total_bill)
print("Total Bill as Integer: ₹", bill_int)

bill_str = str(total_bill)
print("Total Bill as String: ₹" + bill_str)

delivery_charge = random.randint(5, 10)
print("Delivery Charge: ₹", delivery_charge)

final_bill = total_bill + float(delivery_charge)
print("Final Bill Including Delivery Charge: ₹", final_bill)


