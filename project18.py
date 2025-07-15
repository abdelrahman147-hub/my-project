import random
import string
num=[1,2,3,4,5,6,7,8,9]

print("welcome to the password generator!")
number=int(input("enter the total number of characters in the password: "))
letter=int(input("enter the number of letters in the password: "))
numbers=int(input("enter the number of numbers in the password: "))
symbols=int(input("enter the number of symbols in the password: "))
if number== letter+numbers+symbols:
   password=( random.choices(num,k=numbers)+
            random.choices(string.ascii_letters,k=letter)+
            random.choices(string.punctuation,k=symbols)
   )
   random.shuffle(password)
   psa= "".join(str(u) for u in password)
   print(f"your password: {psa}")
else:
    print("invalid input. the sum os letters, numbers and symbols doesn't match the password.")