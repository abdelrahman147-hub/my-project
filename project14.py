items=[]
prices=[]
print("***** welcome to ishop calculator *****")
number_items=int(input("how many items are there in your basket today? "))
if number_items>0:
    print("let's get to counting them...")
    for x in range(0,number_items):
        name=input(f"please tell me the name of the item number {x+1}: ")
        items.append(name)
        price=float(input(f"what is the price of {name}: "))
        prices.append(price)
    choise=input("would you like to see your entire basket items yes or no? ")
    if choise==("yes"):
        print(items)
        see_price=input("would you like to see how much it'll coast yes or no ")
        if see_price=="yes":
            print(sum(prices))
        else:
            input("press inter to exit")
    else:
      input("press inter to exit")
else:
    print("seems like you're not in the mood for shopping today")