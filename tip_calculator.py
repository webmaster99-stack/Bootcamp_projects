print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip // 100
bill_with_tip = bill + (bill * tip_as_percent)
total_bill = bill_with_tip // people

print(f"{total_bill}:.2f")