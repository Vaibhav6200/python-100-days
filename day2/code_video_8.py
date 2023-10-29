# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months

# Create a program using maths and f-strings that tell you how many days, weeks and months we have left if we live until 90 years old

current_age = int(input("What is your current age? "))
days_left = 90*365 - current_age*365
weeks_left = 90*52 - current_age*52
months_left = 90*12 - current_age*12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")