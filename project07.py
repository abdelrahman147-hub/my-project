colors=[]
colors1=input("add the first color you like: ").lower()
colors.append(colors1)
colors2= input("do you want to add more colors? yes or no? ").lower()
if colors2=="yes":
    colors3=input("add another color to your list: ").lower()
    colors.append(colors1 and colors3)
    print(f"the colors you like are: {colors}")
elif colors2=="no":
    colors.append(colors1)
    print(f"the colors you like are {colors}")
else:
    print("please enter yes or no")
