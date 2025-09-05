principal=0
rate=0
time=0

while principal<=0:
    principal=float(input("ENTER THE PRINCIPAL AMOUNT: "))
    if principal<=0:
        print("principal can't be less than or equal to zero ")

while rate<=0:
    rate=float(input("ENTER THE INTEREST RATE: "))
    if rate<=0:
        print("INTEREST rate   can't be less than or equal to zero ")

while time<=0:
    time=int(input("ENTER THE TIME IN YEAR : "))
    if time<=0:
        print(" TIME can't be less than or equal to zero ")

total=principal*pow((1+rate/100),time)
print(f"Balance after {time}year/s:₹{total:.2f} ")