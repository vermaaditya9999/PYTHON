'''
ouput of the code should look like this:

How many items? 2
Enter item 1 name: Apples
Enter quantity: 2
Enter price per item: 50

Enter item 2 name: Rice
Enter quantity: 1
Enter price per item: 120

Items Purchased:
Apples: ₹100.0
Rice: ₹120.0

Total = ₹220.0
No discount applied.
'''
print("🛒".center(40,"-"))
print("Welcome to Av Shop".center(40,"-") )
print("🛒".center(40,"-"))

#ITEM LIST 
Items={
    "pen":10,
    "book":200,
    "craft":50,
    "decoration":100,
    "keyboard":1000,
    "mouse":200,
    "eraser":5,
    "colour":30,
    "register":90
}
print("\n📦Items  Available:")
for item,price in Items.items():
    print(f"{item.title():<20}-₹{price}")



#ITEM 1 
num_item=int(input("Enter how many item you have purchased:"))
prices=[]
items_purchased={} 
user=(input("Enter Item 1 name:"))
user=int(input(f"Enter price of per {user}:"))
#ITEM 2

user=(input("Enter Item 2 name:"))
user=int(input(f"Enter price of  per {user}:"))
Items={
    "pen":10,
    "book":200,
    "craft":50,
    "decoration":100,
    "keyboard":100,
    "mouse":200,
    "eraser":5,
    "colour":30,
    "register":90
}


for i in range(num_item):
    item_name=input(f"Enter name of item{i+1}:")
    quantity=int(input("Enter quantity:"))
    total_price=quantity*user
    items_purchased[user]=total_price 
    item_price=int(input(f"Enter price of 1{item_name}:₹"))
    prices.append(item_price)



price_display="+".join(str(prices)for price in prices)
total=sum(prices)
print(f"\nTotal:{price_display}=₹{total}")





discount=0
if total>=500:
    discount=total*0.10
    final_amount=total-discount
    print(f"You received a 10% discount of ₹{discount}")
else:
    final_amount=total
    print("NO discount applied.")

print(f"Final Amount to pay is:₹{final_amount}")
print("\n🙏 Thank you for shopping at AV Shop! 🙏")
print("Have a great day! 😊")
