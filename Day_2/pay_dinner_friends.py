print("Welcome to the Tip calculator")
total_bill=float(input("What was the total bill ? :$"))
tip_percent=int(input("How much tip would you like to give? 10,12 pr 15? :"))
people_paying=int(input("How many people to spilt the bill? :"))

cost_per_person=total_bill/people_paying
tip_increase=cost_per_person*(tip_percent/100)
final_bill=cost_per_person+tip_increase
print(f"Each person should pay: ${round(final_bill,2)}0")