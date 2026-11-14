# Tip Calculator

print("  Welcome to the Tip Calculator  ".center(50, "$"))
total_bill = float(input("What's your total bill? \n"))
tip_percent = float(
    input("How much tip would like to give in percent? 12 ,15 or 20 \n"))
no_of_splits = int(input("How many people to split the bill? \n"))

bill_per_person = round(
    ((total_bill * (1 + (tip_percent / 100))) / no_of_splits), 2)
print(f"Each person should pay : {bill_per_person}")


# BMI Calculator
# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:
# bmi is equal to the person's weight divided by the person's height squared.
# Convert this sentence into code on line 6.

# BMI = (Wt in kg) / (Ht in m) (MKS)
# BMI = (Wt in lbs) / (Ht in inch) (UCS)
print("Welcome to BMI Calculator")
weight = float(input("Enter the weight of your's in kg: \n"))
height = float(input("Enter the height of your's in cm: \n"))
bmi = (weight) / ((height / 100)**2)
print(f"Your BMI is : {round(bmi)}")
