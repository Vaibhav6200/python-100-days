print("Welcome to tip calculator.")
bill = float(input("What was your total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 15? "))

tip = (tip_percentage / 100) * bill
total_bill = bill + tip


split_count = int(input("How many people to split the bill ? "))
pay_per_person = total_bill/split_count
# final_amount = round(pay_per_person, 2)
final_amount = "{:.2f}".format(pay_per_person)

print(f"Each person should pay: ${final_amount}")
