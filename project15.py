basket=[]
price=[]
print("welcome to ishop calculator")
items=int(input("how many items are there in your basket to day? "))
print("lets's get to counting them....")
for x in range(0,items): 
    item=input("please tell me the name of item ")
    basket.append(item)
    pri=float(input(f"what is the price of {item} "))
    price.append(pri)
see_items=input("would you like to see your entire basket items?(yes/no) ")
if see_items=="yes":
    print(basket)
else:
    print("press enter to exit")
see_price=input("would you like to see how much it'll cost? ")
if see_price=="yes":
    input(f"total price:{sum(price)}")
else:
    input("press enter to exit")