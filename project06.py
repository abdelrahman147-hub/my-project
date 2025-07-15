import random
print("""welcome to the coin gussing game!
choose a method to toss the coin:
1. using random.random()
2. using random.randint()""")
choise=(input("enter your choise (1 or 2)"))
if choise=="1":
   number=random.random()
   if number>=0.5:
      result="heads"
   else:
      result="teals"
elif choise=="2":
   number2=random.randint(0,1)
   if number2==0:
      result="heads"
   else:
     result=("teals")
else:
   ("please enter 1 or 2")

guss=input("enter your guess (heads or tails)").lower()
if guss== (result) :
      print("well done")
else:
      print("sorry you lose")
print(f"the computer choise {result}")

      