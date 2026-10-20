#Electricity Bill Calculator
RATE = 12.90
name = input("Enter customer name: ")

#Validate customer name
if name.strip() == "":
  print("Invalid name. Please try again.")
  name = input("Enter customer name: ")
  
previous = float(input("Enter previous meter reading: "))

#Validating pevious reading
if previous <= 0:
    print("Invalid reading. Please try again.")
    previous = float(input("Enter previous meter reading: "))
    
current = float(input("Enter current meter reading: "))

#Validating current reading
if current <= previous:
    print("Invalid reading. Try again.")
    current = float(input("Enter current meter reading: "))

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
#1. Customer name -- Must not be empty
#2. Previous reading -- Number at least 0
#3. Current reading -- Number at least the previous reading
