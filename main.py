import random
import math

hp = 100
maxhp = 100
tehp = 100
ehp = 80

EdamageType = 0
damageType = 0

def battleFunction(ehp):
  damage=random.randint(10, 30)
  enemydamage=random.randint(0,15)
  #set enemy damage: normal is 0, blocked damage is 1
  global EdamageType
  if EdamageType==1:
    enemydamage=enemydamage*0.5
  #set own damage: normal is 0, crit is 1, reduced is 2
  global damageType
  global hp
  if damageType==1:
    damage=damage*1.75
    print("\nYou did", damage, "elemental damage.")
    hp = (hp - enemydamage)
    print("You took", enemydamage, "damage.")
  elif damageType==2:
    damage=damage*0.5
    print("\nYou did", damage, "elemental damage.")
    hp = (hp - enemydamage)
    print("You took", enemydamage, "damage.")
    ehp = (ehp - damage)

  return ehp,hp

def blockFunction(enemydamage):
  global psickness
  global hp
  hp = (hp - enemydamage)
  print("\nYou took", enemydamage)
  if psickness > 0:
    psickness -= 1
#endHP=battleFunction(ehp,hp)
#endHP[0]=ehp
#endHP[1]=hp
def enemies(enemyelement, enemydamage, damage, damageType, ehp):
  if enemies == 1:
    ehp = 80
    enemydamage = random.randint(10, 20)

def randEncounter(enemyelement, efire, ephysical, ewater, enature, encounter, endable):
  while endable >= 0 and endable <= 10:
    encounter = random.randint(1, 15)
    if encounter >= 14:
      print("An enhancement wisp has appeared. Defeat it to gain strength.")
    elif encounter >= 10:
      print("I can inc")
    else: 
      enemyelement = random.randint(1,4)
    if enemyelement == 1:
      efire = True
      print("A fire enemey has appeared.")
    if enemyelement == 2:
      ewater = True
      print("A water enemey has appeared.")
    if enemyelement == 3:
      enature = True
      print("A nature enemey has appeared.")
    if enemyelement == 4:
      ephysical = True
      print("A physical enemey has appeared.")

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
healing = random.randint(20, 50)
blockcd = 0
psickness = 0

fcombat = [bdamage, fdamage, fcdamage, fndamage, tenemydamage, enemydamage, tbblocked, bblocked, healing, bblocked, psickness]
wcombat = [bdamage, wdamage, wcdamage, wndamage, tenemydamage, enemydamage, tbblocked, bblocked, healing, bblocked, psickness]
ncombat = [bdamage, ndamage, ncdamage, nndamage, tenemydamage, enemydamage, tbblocked, bblocked, healing, bblocked, psickness]
pcombat = [bdamage, pdamage, tenemydamage, enemydamage, tbblocked, bblocked, healing, bblocked, psickness]

enemyelement = 0

next = 1



'''
Idea board/Issue board
Whisps that randomly appear instead of encounters that augment stats as you defeat or caputre them.
Right now, the combat activates twice which is being caused by something related to the fire/water normal combat down in the code. It is not any individual line like it isn't the basic or elemental attacks, it is actually something like the input itself.
'''
F = False
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
else: F = True
#elif z == 0

if F == True:
  print("So fire it is.")
elif W == True:
  print("So water it is.") 
elif N == True:
  print("So nature it is.")
elif P == True:
  print("So physical it is.")

print("\n\n\nLet's get started. Fire, water, and nature follow the normal rock paper scissors triangle. Physical is neutral to all. Try this.\n")

if F == True:
  print("\nA weak nature enemy has appeared.")
elif W == True:
  print("\nA weak fire enemy has appeared.")
elif N == True:
  print("\nA weak water enemy has appeared.")
elif P == True:
  print("\nA weak physical enemy has appeared.")
'''
hp = 100
maxhp = 100
tehp = 100
ehp = 0

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
healing = random.randint(20, 50)
blockcd = 0
psickness = 0
'''
stats = [z, psickness]
abilities = ["basic", "elemental", "block", "heal"]

#All of this atm revolves around fire.
if F == True:
  #ftutorial
  tutorial = 1
while tutorial == 1:
    move = input("Basic, elemental, block, or heal? ")
    if move.lower()== ("basic") or ("b"):
      end = battleFunction(ehp)
      ehp = end[0]
      hp=end[1]
    elif move.lower()== ("elemental") or ("e"):
      battleFunction(ehp,hp,1,0)
    elif move.lower()== ("block"):
      battleFunction(ehp,hp,1,1)
      hp = (hp - bblocked)
      print("\nYou took", bblocked, "damage.")
      blockcd += 1
      print("\nYour shield is cracking.")
      if psickness > 0:
        psickness -= 1
    elif move.lower()== ("heal"):
      healing = random.randint(20, 50)
      if psickness > 0:
        print("You are feeling sick. You can use another potion in", psickness, "turns.")
        psickness -= 1
       #Fix text while healing at max.
      while psickness == 0 and hp < maxhp:
        if hp == maxhp:
          print("Your heal failed.")
          hp = hp
        elif hp < maxhp: 
          hp = (hp + healing)
          if hp > maxhp:
            hp = maxhp
          print("\nYou healed ", healing, " health. You have", hp, "health.")
          psickness += 5
        if psickness > 5:
          psickness = 4
      
      hp = (hp - enemydamage)
    print("\nYou took", enemydamage, "damage.")
    print("\nYou have", hp, " health.")
    print("The enemy has", ehp, "health.")
    #hp = maxhp
    if ehp <= 0:
      tutorial = 0




'''
  if tehp <= 0:
    print("\nGood job. \nThat's odd. The creature turned into dust and was absorbed into you. It looks like the dust is a key to defeat the primal evils of this land. Try to get more.")
    endable = 0
    print("\nAs you venture, my powers and influence wane. You will be on your own from now on but I will be watching over you the best I can.\n\n")
  ehp = 100
  #enemyelement = random.randint(1,4)
  while endable < 10 and next == 1:
    encounter = random.randint(1, 15)
    #It's just fire???
    if encounter < 11:
      ehp = 100
      #next = 0
      #Fire fight
      enemyelement = random.randint(1,4)
      if enemyelement == 1:
        efire = True
        print("\nA fire enemy has appeared.")
        while ehp > 0:
          bdamage = random.randint(10, 30)
          fdamage = random.randint(10, 30)
          fcdamage = fdamage*1.5
          fndamage = fdamage*0.75
          move = input("Basic, elemental, block, or heal? ")
          if move.lower()== ("basic") or ("b"):
            ehp = (ehp - bdamage)
            print("\nYou did", bdamage, "damage.")
            hp = (hp -  enemydamage)
            print("\nYou took", enemydamage, "damage.")
            if psickness > 0:
              psickness -= 1
          if move.lower()== ("elemental"):
            ehp = (ehp - fdamage)
            print("\nYou did", fdamage, "elemental damage.")
            hp = (hp -  enemydamage)
            print("You took", enemydamage, "damage.")
            if psickness > 0:
              psickness -= 1
          if move.lower()== ("block"):
            hp = (hp - bblocked)
            print("\nYou took", bblocked, "damage.")
            blockcd += 1
            print("\nYour shield is cracking.")
            if psickness > 0:
              psickness -= 1
          if move.lower()== ("heal"):
            healing = random.randint(20, 50)
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
            
            hp = (hp - enemydamage)
            print("\nYou took", enemydamage, "damage.")
          print("\nYou have", hp, " health.")
          print("The enemy has", ehp, "health.")
        if ehp >= 0:
           print("Good job but you can't stop now.")
           print("\nYou collected more dust.")
           endable += 1
           print(endable)
           next = 1

    elif enemyelement == 2:
      ewater = True
      print("\nA water enemy has appeared.")
      while ehp > 0:
          bdamage = random.randint(10, 30)
          fdamage = random.randint(10, 30)
          fcdamage = fdamage*1.5
          fndamage = fdamage*0.75
          enemydamage = random.randint(10, 25)
          move = input("Basic, elemental, block, or heal? ")
          if move.lower()== ("basic") or ("b"):
            ehp = (ehp - bdamage)
            print("\nYou did", bdamage, "damage.")
            hp = (hp -  enemydamage)
            print("\nYou took", enemydamage, "damage.")
            if psickness > 0:
              psickness -= 1
          if move.lower()== ("elemental") or ("e"):
            ehp = (ehp - fndamage)
            print("\nYou did", fndamage, "elemental damage.")
            hp = (hp -  enemydamage)
            print("You took", enemydamage, "damage.")
            if psickness > 0:
              psickness -= 1
          if move.lower()== ("block"):
            hp = (hp - bblocked)
            print("\nYou took", bblocked, "damage.")
            blockcd += 1
            print("\nYour shield is cracking.")
            if psickness > 0:
              psickness -= 1
          if move.lower()== ("heal") or ("h"):
            healing = random.randint(20, 50)
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
            
            hp = (hp - enemydamage)
            print("\nYou took", enemydamage, "damage.")
          print("\nYou have", hp, " health.")
          print("The enemy has", ehp, "health.")
          if ehp >= 0:
           print("Good job but you can't stop now.")
           print("\nYou collected more dust.")
           endable + 1
           print(endable)
           next = 1
      
    elif enemyelement == 3:
     enature = True
     print("A nature enemy has appeared.")
      


      
    elif enemyelement == 4:
     ephysical = True
     print("A physical enemy has appeared.")
     print(encounter)
    elif encounter == 11 or 12 or 13:
      #next = 0

      buff = input("\nI have enough strength to strengthen you slightly. Will it be strength, elemental magic, or health?")
      if buff.lower()==("strength") or ("s"):
        bdamage = bdamage + 5
      if buff.lower()==("elemental") or ("e"):
        fdamage = fdamage + 5
      if buff.lower()==("elemental magic"):
        fdamage = fdamage + 5
      if buff.lower()==("health"):
        hp = hp + 25
      if buff.lower()==("hp"):
        hp = hp + 25
        print(encounter)
        next = 1
      #elif 

    elif encounter > 13:
      #next = 0
      print("An enhancement whisp has appeared. If you defeat it before it deems you unworthy, it will allow you to augment your abilities.")
      worth = 5
      print(encounter)
      #while worth > 0:
print(encounter)'''