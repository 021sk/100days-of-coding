print ("welcom to tip calculator")
bill = float(input("what was was total bill: $"))
tip = int(input("what percentage do you want to tip?10 15 20: "))
peaople = int(input("how many are you"))
bill_with_tip = bill + bill * tip / 100
bill_per_person = bill_with_tip / peaople
final_amount = round(bill_per_person, 2)
print(f"each person should pay: ${final_amount}")