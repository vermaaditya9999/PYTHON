rent = int(input("ENTER the  HOSTEL/ FLAT rent="))
food = int(input("ENTER the amount of food ordered="))
electricity_spend = int(input("ENTER the  total of electricity spend="))
charge_per_unit = int(input("ENTER the charge per unit="))
person = int(input("ENTER the number of person living in HOSTEL/FLAT RENT="))


total_bill = electricity_spend*charge_per_unit
output = (food+rent+total_bill)//person

print("per person will pay", output)