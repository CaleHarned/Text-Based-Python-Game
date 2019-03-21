#i couldnt get the tuple to work so i had to use it as a list
import random
print("Greetings Travler and welcome to the Battle of Helms Deep. Here are the options for the game:")
print("1. Create a new charactor.")
print("2. Learn the rules.")
print("3. Load a previous charactor.")
print("4. Quit the game.")
menuChoice=0
while menuChoice !="0":
    menuChoice=input(str("Please ENTER the number of the option you want to choose:"))
    if menuChoice=="1":
        charactorName=0
        charactorClass=0
        maxHitpoints=20
        currentHitpoints=maxHitpoints
        damageOutput=4
        potionCount=2
        Exp=0
        print("-"*40)
        print("The Battle of Helms Deep is upon you. The 1000's of orcs running twards the wall. It is your duty to defend it. Kill as many as you can!")
        print("-"*40)
        while charactorClass==0:
            print("Please choose a class for you to play as.")
            print("1.Human")
            print("2.Elf")
            print("3.Dwarf")
            print("4.Hobbit")
            charactorClass=input(str("Please Enter the number of the desired class:"))
            if charactorClass == "1":
                maxHitpoints=maxHitpoints+5
                damageOutput=damageOutput+1
            if charactorClass == "2":
                maxHitpoints=maxHitpoints-2
            if charactorClass == "3":
                damageOutput=damageOutput+1
            if charactorClass == "4":
                damageOutput=damageOutput-1
            if charactorClass != "1" and charactorClass != "2" and charactorClass != "3" and charactorClass != "4":
                print("Please try your input again.")
                print("-"*40)
                charactorClass=0
        print("-"*40)
        charactorName=input(str("Please give your charactor a name:"))
        print("-"*40)
        #for opition 3 copy from here down
        print("Time to kill some orcs!")
        #combat
        maxOrchitpoints=12
        orcHp=maxOrchitpoints
        orcDmg=4
        while (Exp < 40):
             print("-"*40)
             #dialog based on exp
             if Exp == 0:
                 print("A single orc comes your way looking for blood.")
             if Exp == 10:
                 print("The orcs friend sees you slay him. He comes at you to avange his fallen comrade.")
             if Exp == 20:
                 print("Another orc comes over the horizon looking to kill you.")
             if Exp == 30:
                 print ("There is always another orc. You fix your sight to the closest one.")
             print("What would you like to do?")
             print("1. ATTACK!!!")
             print("2. RUN AWAY!!!")
             print("3. Use a potion.")
             print("-"*40)
             myAction=input(str("Please Enter the number of the desired choice:"))
             print("-"*40)
             if myAction=="1":#attacking
                 myAttack=random.randint (1,20)
                 #misses
                 if charactorClass=="1" and myAttack <7:
                     print("The orc swiftly evades your attack.")
                 if charactorClass=="2" and myAttack<6:
                     print("The orc swiftly evades your attack.")
                 if charactorClass=="3"and myAttack <8:
                     print("The orc swiftly evades your attack.")
                 if charactorClass=="4" and myAttack <5:
                     print("The orc swiftly evades your attack.")
                 #hits
                 if charactorClass=="1" and myAttack >=7 and myAttack <20:
                     print ("You slash at the orc and make a succesfull hit!")
                     orcHp=orcHp-damageOutput
                 if charactorClass=="2" and myAttack>=6 and myAttack <20 :
                     print ("You slash at the orc and make a succesfull hit!")
                     orcHp=orcHp-damageOutput
                 if charactorClass=="3" and myAttack>=8 and myAttack <20 :
                     print ("You slash at the orc and make a succesfull hit!")
                     orcHp=orcHp-damageOutput
                 if charactorClass=="4" and myAttack>=5 and myAttack <20 :
                     print ("You slash at the orc and make a succesfull hit!")
                     orcHp=orcHp-damageOutput
                 if myAttack==20:
                     print("You muster all the might you can to deliver a menacing blow!")
                     orcHp=orcHp-damageOutput*2
                 if orcHp>0:       
                     orcAtk=random.randint (1,20)
                     if orcAtk <7:
                         print("The orc attempts to hit you with his club but you are nimble enough to evade it.")
                     if orcAtk >=7:
                         print ("The orc slams the club into you dealing 3 damage!")
                         currentHitpoints=currentHitpoints-3
                         print("Your health is now at:"+str(currentHitpoints))    
                 if orcHp<=0:
                     print("-"*40)
                     print ("The orc has been slain by your hands!")
                     Exp=Exp+10
                     #reset Orc
                     x=0
                     while x<12 and orcHp<maxOrchitpoints:
                         orcHp=orcHp+1
                         x=x+1
                     cont=input(str("Would you like to Save and Quit? Enter yes or no:"))
                     if cont=="yes":
                         playerCharactor = charactorName + "\n" + str(charactorClass) + "\n" + str(Exp) + "\n" + str(maxHitpoints) + "\n" + str(currentHitpoints) + "\n" + str(potionCount) + "\n" + str(damageOutput)
                         save = open(charactorName+".txt", "w")
                         save.write(playerCharactor)
                         save.close()
                         quit()

             if myAction=="2":#running
                 runValue=random.randint (1,5)
                 if runValue ==1:
                     print("You successfully get away and a random healer heals you for ten health points.")
                     if currentHitpoints<maxHitpoints:
                        while y<10 and currentHitpoints<maxHitpoints:
                             y=0
                             currentHitpoints=currentHitpoints+1
                             y=y+1
                        print("Your HP is "+currentHitpoints)
                 if runValue != 1:
                     print ("You fail to run away. The orc then goes for attack")
                     orcAtk=random.randint (1,20)
                     if orcAtk <7:
                         print("The orc attempts to hit you with his club but you are nimble enough to evade it.")
                     if orcAtk >=7:
                         print ("The orc slams the club into you dealing 3 damage!")
                         currentHitpoints=currentHitpoints-3
                         print("Your health is now at:"+currentHitpoints)

             if myAction=="3":#potion
                 print("You check your items and looks like you have *"+str(potionCount)+"* potions left.")
                 if potionCount >= 1:
                     print("You drink one of your potions to heal 5 health points")
                     x=0
                     while x<5 and currentHitpoints<maxHitpoints:
                         currentHitpoints=currentHitpoints+1
                         x=x+1
                     print("Your health is now at:"+str(currentHitpoints))
                     potionCount=otionCount-1
                 if potionCount == 0:
                     print("Damn, you sould have bought more. Oh well, back to the fight")
             if myAction != "1" and myAction != "2" and myAction != "3":
                 print("Please try your input again.")
        if Exp == 40:#boss
            print("As you kill the last one, The Uruk-Hai rears his ugly mug and he's looking right at you. Its time you take this piece of crap out.")
            bossHp=16
            bossDmg=5
            print("What would you like to do?")
            print("1. ATTACK!!!")
            print("2. RUN AWAY!!!")
            print("3. Use a potion.")
            print("-"*40)
            bossAction=input(str("Please Enter the number of the desired choice:"))
            print("-"*40)
            if bossAction=="1":#attacking
                myBossAttack=random.randint (1,20)
                #misses
                if charactorClass=="1" and myBossAttack <7:
                    print("The orc swiftly evades your attack.")
                if charactorClass=="2" and myBossAttack<6:
                    print("The orc swiftly evades your attack.")
                if charactorClass=="3"and myBossAttack <8:
                    print("The orc swiftly evades your attack.")
                if charactorClass=="4" and myBossAttack <5:
                    print("The orc swiftly evades your attack.")
                 #hits
                if charactorClass=="1" and myBossAttack >=7 and myBossAttack <20:
                    print ("You slash at the Uruk-Hai and make a succesfull hit!")
                    bossHp=bossHp-damageOutput
                if charactorClass=="2" and myBossAttack>=6 and myBossAttack <20 :
                    print ("You slash at the Uruk-Hai and make a succesfull hit!")
                    bossHp=bossHp-damageOutput
                if charactorClass=="3" and myBossAttack>=8 and myBossAttack <20 :
                    print ("You slash at the Uruk-Hai and make a succesfull hit!")
                    bossHp=bossHp-damageOutput
                if charactorClass=="4" and myBossAttack>=5 and myBossAttack <20 :
                    print ("You slash at the Uruk-Hai and make a succesfull hit!")
                    bossHp=bossHp-damageOutput
                if myAttack==20:
                    print("You muster all the might you can to deliver a menacing blow!")
                    bossHp=bossHp-damageOutput*2
                if bossHp>0:       
                    bossAtk=random.randint (1,20)
                    if bossAtk <9:
                        print("The Uruk-Hai attempts to hit you with his club but you are nimble enough to evade it.")
                    if bossAtk >=9:
                        print ("The Uruk-Hai slams the club into you dealing 5 damage!")
                        currentHitpoints=currentHitpoints-bossDmg
                        print("Your health is now at:"+str(currentHitpoints))    
                if bossHp<=0:
                    print("You have slain the Uruk-Hai. With the orcs leader dead, they begin a retreat. Well done Hero.")
            if bossAction=="2":#running
                runValue=random.randint (1,5)
                if runValue ==1:
                    print("You successfully get away and a random healer heals you for ten health points.")
                    if currentHitpoints<maxHitpoints:
                        while y<10 and currentHitpoints<maxHitpoints:
                            y=0
                            currentHitpoints=currentHitpoints+1
                            y=y+1
                        print("Your HP is "+currentHitpoints)
                if runValue != 1:
                    print ("You fail to run away. The Uruk-Hai then goes for attack")
                    orcAtk=random.randint (1,20)
                    if orcAtk <7:
                        print("The Uruk-Hai attempts to hit you with his club but you are nimble enough to evade it.")
                    if orcAtk >=7:
                        print ("The Uruk-Hai slams the club into you dealing 5 damage!")
                        currentHitpoints=currentHitpoints-3
                        print("Your health is now at:"+currentHitpoints)

            if bossAction=="3":#potion
                print("You check your items and looks like you have *"+str(potionCount)+"* potions left.")
                if potionCount >= 1:
                    print("You drink one of your potions to heal 5 health points")
                    x=0
                    while x<5 and currentHitpoints<maxHitpoints:
                        currentHitpoints=currentHitpoints+1
                        x=x+1
                    print("Your health is now at:"+str(currentHitpoints))
                    potionCount=otionCount-1
                if potionCount == 0:
                    print("Damn, you sould have bought more. Oh well, back to the fight")
        
    if menuChoice=="2": 
        print("The rules of the game are simple.")
        print("You start the game with 20 Health and your goal is to kill a lot of orcs. You will have a race that will allow you certain buffs. You will be greanted 2 healing potions that both heal 5 health. You have the option to run during combat, if you succed, you will be healed for 10 hp. If you fail, The orc you are running from attacks you. Good Luck.")



        
    if menuChoice=="3":
        charactorName=input(str("Please Enter the EXACT name of the charactor's save file:"))
        file=open(charactorName+".txt","r")
        lines = file.readlines()
        saveList = []
        for line in lines:
            line = line.rstrip()
            saveList.append(line)
        charactorName = saveList[0]
        charactorClass = saveList[1]
        Exp = int(saveList[2])
        maxHitpoints = int(saveList[3])
        currentHitpoints = int(saveList[4])
        potionCount=int(saveList[5])
        damageOutput=int(saveList[6])
        

        print("Time to kill some orcs!")
        #combat
        maxOrchitpoints=12
        orcHp=maxOrchitpoints
        orcDmg=4
        while (Exp < 40):
             print("-"*40)
             #dialog based on exp
             if Exp == 0:
                 print("A single orc comes your way looking for blood.")
             if Exp == 10:
                 print("The orcs friend sees you slay him. He comes at you to avange his fallen comrade.")
             if Exp == 20:
                 print("Another orc comes over the horizon looking to kill you.")
             if Exp == 30:
                 print ("There is always another orc. You fix your sight to the closest one.")
             print("What would you like to do?")
             print("1. ATTACK!!!")
             print("2. RUN AWAY!!!")
             print("3. Use a potion.")
             print("-"*40)
             myAction=input(str("Please Enter the number of the desired choice:"))
             print("-"*40)
             if myAction=="1":#attacking
                 myAttack=random.randint (1,20)
                 #misses
                 if charactorClass=="1" and myAttack <7:
                     print("The orc swiftly evades your attack.")
                 if charactorClass=="2" and myAttack<6:
                     print("The orc swiftly evades your attack.")
                 if charactorClass=="3"and myAttack <8:
                     print("The orc swiftly evades your attack.")
                 if charactorClass=="4" and myAttack <5:
                     print("The orc swiftly evades your attack.")
                 #hits
                 if charactorClass=="1" and myAttack >=7 and myAttack <20:
                     print ("You slash at the orc and make a succesfull hit!")
                     orcHp=orcHp-damageOutput
                 if charactorClass=="2" and myAttack>=6 and myAttack <20 :
                     print ("You slash at the orc and make a succesfull hit!")
                     orcHp=orcHp-damageOutput
                 if charactorClass=="3" and myAttack>=8 and myAttack <20 :
                     print ("You slash at the orc and make a succesfull hit!")
                     orcHp=orcHp-damageOutput
                 if charactorClass=="4" and myAttack>=5 and myAttack <20 :
                     print ("You slash at the orc and make a succesfull hit!")
                     orcHp=orcHp-damageOutput
                 if myAttack==20:
                     print("You muster all the might you can to deliver a menacing blow!")
                     orcHp=orcHp-damageOutput*2
                 if orcHp>0:       
                     orcAtk=random.randint (1,20)
                     if orcAtk <7:
                         print("The orc attempts to hit you with his club but you are nimble enough to evade it.")
                     if orcAtk >=7:
                         print ("The orc slams the club into you dealing 3 damage!")
                         currentHitpoints=currentHitpoints-3
                         print("Your health is now at:"+str(currentHitpoints))    
                 if orcHp<=0:
                     print("-"*40)
                     print ("The orc has been slain by your hands!")
                     Exp=Exp+10
                     #reset Orc
                     x=0
                     while x<12 and orcHp<maxOrchitpoints:
                         orcHp=orcHp+1
                         x=x+1
                     cont=input(str("Would you like to Save and Quit? Enter yes or no:"))
                     if cont=="yes":#fix
                         playerCharactor = charactorName + "\n" + str(charactorClass) + "\n" + str(Exp) + "\n" + str(maxHitpoints) + "\n" + str(currentHitpoints) + "\n" + str(potionCount) + "\n" + str(damageOutput)
                         save = open(charactorName+".txt", "w")
                         save.write(playerCharactor)
                         save.close()
                         quit()

             if myAction=="2":#running
                 runValue=random.randint (1,5)
                 if runValue ==1:
                     print("You successfully get away and a random healer heals you for ten health points.")
                     if currentHitpoints<maxHitpoints:
                        while y<10 and currentHitpoints<maxHitpoints:
                             y=0
                             currentHitpoints=currentHitpoints+1
                             y=y+1
                        print("Your HP is "+currentHitpoints)
                 if runValue != 1:
                     print ("You fail to run away. The orc then goes for attack")
                     orcAtk=random.randint (1,20)
                     if orcAtk <7:
                         print("The orc attempts to hit you with his club but you are nimble enough to evade it.")
                     if orcAtk >=7:
                         print ("The orc slams the club into you dealing 3 damage!")
                         currentHitpoints=currentHitpoints-3
                         print("Your health is now at:"+currentHitpoints)

             if myAction=="3":#potion
                 print("You check your items and looks like you have *"+str(potionCount)+"* potions left.")
                 if potionCount >= 1:
                     print("You drink one of your potions to heal 5 health points")
                     x=0
                     while x<5 and currentHitpoints<maxHitpoints:
                         currentHitpoints=currentHitpoints+1
                         x=x+1
                     print("Your health is now at:"+str(currentHitpoints))
                     potionCount=otionCount-1
                 if potionCount == 0:
                     print("Damn, you sould have bought more. Oh well, back to the fight")
             if myAction != "1" and myAction != "2" and myAction != "3":
                 print("Please try your input again.")
        if Exp == 40:#boss
            print("As you kill the last one, The Uruk-Hai rears his ugly mug and he's looking right at you. Its time you take this piece of crap out.")
            bossHp=16
            bossDmg=5
            print("What would you like to do?")
            print("1. ATTACK!!!")
            print("2. RUN AWAY!!!")
            print("3. Use a potion.")
            print("-"*40)
            bossAction=input(str("Please Enter the number of the desired choice:"))
            print("-"*40)
            if bossAction=="1":#attacking
                myBossAttack=random.randint (1,20)
                #misses
                if charactorClass=="1" and myBossAttack <7:
                    print("The orc swiftly evades your attack.")
                if charactorClass=="2" and myBossAttack<6:
                    print("The orc swiftly evades your attack.")
                if charactorClass=="3"and myBossAttack <8:
                    print("The orc swiftly evades your attack.")
                if charactorClass=="4" and myBossAttack <5:
                    print("The orc swiftly evades your attack.")
                 #hits
                if charactorClass=="1" and myBossAttack >=7 and myBossAttack <20:
                    print ("You slash at the Uruk-Hai and make a succesfull hit!")
                    bossHp=bossHp-damageOutput
                if charactorClass=="2" and myBossAttack>=6 and myBossAttack <20 :
                    print ("You slash at the Uruk-Hai and make a succesfull hit!")
                    bossHp=bossHp-damageOutput
                if charactorClass=="3" and myBossAttack>=8 and myBossAttack <20 :
                    print ("You slash at the Uruk-Hai and make a succesfull hit!")
                    bossHp=bossHp-damageOutput
                if charactorClass=="4" and myBossAttack>=5 and myBossAttack <20 :
                    print ("You slash at the Uruk-Hai and make a succesfull hit!")
                    bossHp=bossHp-damageOutput
                if myAttack==20:
                    print("You muster all the might you can to deliver a menacing blow!")
                    bossHp=bossHp-damageOutput*2
                if bossHp>0:       
                    bossAtk=random.randint (1,20)
                    if bossAtk <9:
                        print("The Uruk-Hai attempts to hit you with his club but you are nimble enough to evade it.")
                    if bossAtk >=9:
                        print ("The Uruk-Hai slams the club into you dealing 5 damage!")
                        currentHitpoints=currentHitpoints-bossDmg
                        print("Your health is now at:"+str(currentHitpoints))    
                if bossHp<=0:
                    print("You have slain the Uruk-Hai. With the orcs leader dead, they begin a retreat. Well done Hero.")
            if bossAction=="2":#running
                runValue=random.randint (1,5)
                if runValue ==1:
                    print("You successfully get away and a random healer heals you for ten health points.")
                    if currentHitpoints<maxHitpoints:
                        while y<10 and currentHitpoints<maxHitpoints:
                            y=0
                            currentHitpoints=currentHitpoints+1
                            y=y+1
                        print("Your HP is "+currentHitpoints)
                if runValue != 1:
                    print ("You fail to run away. The Uruk-Hai then goes for attack")
                    orcAtk=random.randint (1,20)
                    if orcAtk <7:
                        print("The Uruk-Hai attempts to hit you with his club but you are nimble enough to evade it.")
                    if orcAtk >=7:
                        print ("The Uruk-Hai slams the club into you dealing 5 damage!")
                        currentHitpoints=currentHitpoints-3
                        print("Your health is now at:"+currentHitpoints)

            if bossAction=="3":#potion
                print("You check your items and looks like you have *"+str(potionCount)+"* potions left.")
                if potionCount >= 1:
                    print("You drink one of your potions to heal 5 health points")
                    x=0
                    while x<5 and currentHitpoints<maxHitpoints:
                        currentHitpoints=currentHitpoints+1
                        x=x+1
                    print("Your health is now at:"+str(currentHitpoints))
                    potionCount=otionCount-1
                if potionCount == 0:
                    print("Damn, you sould have bought more. Oh well, back to the fight")

    if menuChoice=="4":
        quit()

    if menuChoice!="1" and menuChoice!="2" and menuChoice!="3" and menuChoice!="4":
        print("Try again please")
