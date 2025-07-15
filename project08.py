library=[]
book1=input("enter the name of a book you own: ")
library.append(book1)
book2=input("enter the name of another book you own (or press'enter' or skip):")
if book2:
    library.append(book2)
    print(f"your library:{library}")

else:
    print(f"your library:{library}")
wish_list=[]
book3=input("enter the name of a book you wish to have in the future: ")
wish_list.append(book3)
book4=input("enter the name of another book you wish to have in the future (or press'enter' or skip): ")
if book4:
    wish_list.append(book4)
    print(f"your whish list:{wish_list}")
else:
    print(f"your whish list:{wish_list}")
book5=input("enter the name of a book from your wishlist that you've acquired (or press'enter' or skip): ")
if book5:
    library.append(book5)
    wish_list.remove(book5)
    final_library=library+(wish_list)
    print(f"""updated library:{library}
         updated wishlist:{wish_list}""" )
else:
    print(f"""updated library:{library}
         updated wishlist:{wish_list}""" )
book6=input("enter the name of a book from your library you wish to donate (or press'enter' or skip): ")
if book6:
    library.remove(book6)
    print(f"final library after donations:{library}")
else:
    print(f"final library after donations:{library}")