#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
bill = (input("What was the total bill? $"))
tip_percentage = (input("What percentage tip would you like to give? 10, 12, or 15? "))
calculation = int(tip_percentage) / 100
# print(calculation)
total = int(bill) * calculation
final_tip = total
overall_bill = int(bill) + final_tip
split_bill = (input("How many people to split the bill? " ))
final_bill = float(overall_bill) / int(split_bill)
result = round(final_bill , 2)
print(f"Each person should pay: ${result}")
print(f"{result:.2f}")