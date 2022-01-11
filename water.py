'''import random
import math
next = 1
''''''
Idea board
Whisps that randomly appear instead of encounters that augment stats as you defeat or caputre them.
'''
'''F = False
W = False
N = False
P = False
efire = False
ewater = False
enature = False
ephysical = False

endable = -1

z = input("Which element? \nFire, Water, Nature, or Physical?\n")

if z.lower()=="fire" or z.lower() == "f":
  F = True
elif z.lower() == "water" or z.lower() == "w":
  W = True
elif z.lower() == "nature" or z.lower() == "n":
  N = True
elif z.lower() == "physical" or z.lower() == "p":
  P = True
#elif z == 0

if F == True:
  print("So fire it is?")
elif W == True:
  print("So water it is?") 
elif N == True:
  print("So nature it is?")
elif P == True:
  print("So physical it is")

print("\n\nLet's get started. Fire, water, and nature follow the normal rock paper scissors triangle. Physical is neutral to all. Try this.\n")

if F == True:
  print("\nA weak nature enemy has appeared.")
elif W == True:
  print("\nA weak fire enemy has appeared.")
elif N == True:
  print("\nA weak water enemy has appeared.")
elif P == True:
  print("\nA weak physical enemy has appeared.")

hp = 100
maxhp = 100
tehp = 100
ehp = 100

bdamage = random.randint(10, 30)

fdamage = random.randint(10, 30)
fcdamage = fdamage*1.5
fndamage = fdamage*0.75
wdamage = random.randint(10, 30)
wcdamage = wdamage*1.5
wndamage = wdamage*0.75
ndamage = random.randint(10, 30)
ncdamage = ndamage*1.5
nndamage = ndamage*0.75
pdamage = random.randint(5, 50)

tenemydamage = random.randint(5, 15)
tbblocked = tenemydamage*.5
enemydamage = random.randint(10, 25)
bblocked = enemydamage*.5
healing = random.randint(5, 50)
blockcd = 0
psickness = 0

stats = [z, psickness]
abilities = ["basic", "elemental", "block", "heal"]

if W == True:
  while tehp > 0:
    move = input("Basic, elemental, block, or heal? ")
    if move.lower()== ("basic"):
      tehp = (tehp - bdamage)
      print("\nYou did", bdamage, "damage.")
      hp = (hp -  tenemydamage)
      print("\nYou took", tenemydamage, "damage.")
      if psickness > 0:
        psickness -= 1
    if move.lower()== ("elemental"):
      tehp = (tehp - wcdamage)
      print("\nYou did", wcdamage, "elemental damage.")
      hp = (hp -  tenemydamage)
      print("You took", tenemydamage, "damage.")
      if psickness > 0:
       psickness -= 1
    if move.lower()== ("block"):
      hp = (hp - tbblocked)
      print("\nYou took", tbblocked, "damage.")
      blockcd += 1
      print("\nYour shield is cracking.")
      if psickness > 0:
        psickness -= 1
    if move.lower()== ("heal"):
      if psickness > 0:
        print("You are feeling sick. You can use another potion in", psickness, "turns.")
        psickness -= 1
  #Fix text while healing at max.
      while psickness == 0 and hp < maxhp:
        if hp == maxhp:
          print("Your heal failed.")
          hp = hp - 1
        if hp < maxhp: 
          hp = (hp + healing)
          if hp > maxhp:
            hp = maxhp
          print("\nYou healed ", healing, " health. You have", hp, "health.")
          psickness += 5
        if psickness > 5:
          psickness = 4
      
      hp = (hp - tenemydamage)
      print("\nYou took", tenemydamage, "damage.")
    print("\nYou have", hp, " health.")
    print("The enemy has", tehp, "health.")

if tehp <= 0:
  print("\nGood job. \nThat's odd. The creature turned into dust and was absorbed into you. It looks like the dust is a key to defeat the primal evils of this land. Try to get more.")
  endable = 0
  print("\nAs you venture, my powers and influence wane. You will be on your own from now on but I will be watching over you the best I can.")

enemyelement = random.randint(1,4)
while endable < 10:
  encounter = random.randint(1, 15)

  if encounter < 11:
    if enemyelement == 1:
      efire = True
      print("A fire enemy has appeared.")
    elif enemyelement == 2:
      ewater = True
      print("A water enemy has appeared.")
    elif enemyelement == 3:
      enature = True
      print("A nature enemy has appeared.")
    elif enemyelement == 4:
      ephysical = True
      print("A physical enemy has appeared.")

  if encounter == 11 or 12 or 13:

    buff = input("\nI have enough strength to strengthen you slightly. Will it be strength, elemental magic, or health?")
    if buff.lower()==("Strength"):
      bdamage = bdamage + 5
    if buff.lower()==("Elemental"):
      wdamage = wdamage + 5
    if buff.lower()==("Elemental magic"):
      wdamage = wdamage + 5
    if buff.lower()==("Health"):
      hp = hp + 25
    if buff.lower()==("Hp"):
      hp = hp + 25
    #elif 

  if encounter > 13:
    print("An enhancement whisp has appeared. If you defeat it before it deems you unworthy, it will allow you to augment your abilities.")
    worth = 5
    #while worth > 0:
    '''