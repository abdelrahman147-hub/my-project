mission=input("enter your tasks today.by a comma: ").split(", ")
yes_done=[]
no_done=[]
for tasks in mission:
    done=input(f"did you finish {tasks} ")
    if done=="no":
      no_done.append(tasks)
      print("try to not put it off")
    else:
       yes_done.append(tasks)
       print("nice job")
    print("-------------")
tasks=input("do you want to see your today's progress?(yes \ no) ")
if tasks=="yes":
    print(f""" ***** done mission *****
        {yes_done}""")
    print(f"""***** ongoing mission *****
        {no_done}""")
else:
    input("press enter to exit")