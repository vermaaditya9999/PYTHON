operator=input("Enter an operator:")
num1=int(input("Enter the 1 number"))
num2=int(input("Enter the 2 number"))

if operator=="+":
   result= num1 + num2
   print(result)
elif operator=="-":
    result= num1 - num2
    print(result)
elif operator=="*":
    result= num1 * num2
    print(result)
elif operator=="/":
    result= num1 / num2
    print(result)
elif operator=="%":
    result= num1 % num2
    print(result)


else:
    print("its not a valid operator")


