names=input("enter the first and last name of your friends separated by a comma: ").split(", ")
abbreviated_names=[]
for name in names:
    name_parts=name.split()
    print(name_parts)
    first_name=name_parts[0]
    last_name=name_parts[1]
    first_initiol=first_name[0]
    last_initiol=last_name[0]
    abbreviated=first_initiol+ "."+last_initiol+"."
    abbreviated_names.append(abbreviated)
print("abbreviated names:")
for x in abbreviated_names:
        print(x)