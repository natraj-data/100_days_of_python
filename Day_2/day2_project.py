# Tip Calculator

print("  Welcome to the Tip Calculator  ".center(50, "$"))
total_bill = float(input("What's your total bill? \n"))
tip_percent = float(
    input("How much tip would like to give in percent? 12 ,15 or 20 \n"))
no_of_splits = int(input("How many people to split the bill? \n"))

bill_per_person = round(
    ((total_bill * (1 + (tip_percent / 100))) / no_of_splits), 2)

print(f"Each person should pay : {bill_per_person}")
