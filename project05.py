print("""

╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╭╮
╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯╰╮╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱┃┃
╭╮╭╮╭┳━━┫┃╭━━┳━━┳╮╭┳━━╮╰╮╭╋━━╮╭╮╭┳╮╱╭╮┃┃╭━━┳━╮╭━╯┃
┃╰╯╰╯┃┃━┫┃┃╭━┫╭╮┃╰╯┃┃━┫╱┃┃┃╭╮┃┃╰╯┃┃╱┃┃┃┃┃╭╮┃╭╮┫╭╮┃
╰╮╭╮╭┫┃━┫╰┫╰━┫╰╯┃┃┃┃┃━┫╱┃╰┫╰╯┃┃┃┃┃╰━╯┃┃╰┫╭╮┃┃┃┃╰╯┃
╱╰╯╰╯╰━━┻━┻━━┻━━┻┻┻┻━━╯╱╰━┻━━╯╰┻┻┻━╮╭╯╰━┻╯╰┻╯╰┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
      """)
print("welcome to my land")
doors=input("""there are two doors in front of you. 🚪 a red door and 🚪 a blue door
 which door do you want to open? \n""").lower()
if doors=="red":
    print("great! now you entered a room.")
    boxs=input("""you found three boxes:📦 white,📦 black,📦 green
    which box do you open \n""").lower()
    if boxs=="white":
     print("oops! you opened a box filled with snakes 🐍🐍🐍")
    elif boxs=="black":
     print("oops!you opened a box filled with spiders🕷️🕷️🕷️")
    elif boxs=="green":
      print("congratulations! you found the treasure!🪙🪙🪙")
    else:
      print("invalid choice🙅🙅🙅")
elif doors== "blue":
  print("""oops! you chose the crocodile door🐊🐊🐊.
        game over!""")
else:
  print("invalid choice🙅🙅🙅")