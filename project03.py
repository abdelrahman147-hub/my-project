number1= input("please type your length")
number2= input("please type your width")
number3= input("how much for 1 meter")
length=float (number1)
width= float (number2)
price= float(number3)
area= length*width
str_area= str(area)
coast= area*price
str_coast=str(coast)
print ("area" + str_area)
print ("coast" + str_coast)

