# Inputs we need from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per unit 
# Persons living in room/flat

## Output
# Total amount you've to pay is

rent = int(input("Enter the rent of hostel/PG = "))
food = int(input("Enter the amount of food orderd ="))
units_per_month = int(input("Enter total number of units use per month = "))
charge_per_unit = int(input("Enter charge per unit = "))
persons = int(input("Enter the number of persons living in room =" ))

total_electricity_bill = units_per_month * charge_per_unit

output = (food + rent + total_electricity_bill) // persons

print("Each person will pay = ", output)