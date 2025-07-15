print("welcome to place the rabbit")
fildes=[['🍃', '🍃', '🍃'],['🍃', '🍃', '🍃'],['🍃', '🍃', '🍃'] ]
print(f"{fildes[0]} \n{fildes[1]} \n{fildes[2]}")
numbers=input("where should the rabbit go?🐇 \nplease choose a row and a column ")
row=int(numbers[0])
column=int(numbers[1])
fildes[row-1][column-1]="🐇"
print("success...")
print(f"{fildes[0]} \n{fildes[1]} \n{fildes[2]}")