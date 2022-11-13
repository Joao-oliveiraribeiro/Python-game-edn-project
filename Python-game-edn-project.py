import sys
import os
import random



name = "warrior"
maxhp = 32
wp = 5
maxmp = 5
mp = 5
ap = 2
init = 2



name2 = "priest"
maxhp2 = 20
wp2 = 2
maxmp2 = 25
mp2 = 25
ap2 = 0
init2 = 6



name3 = "orc_warrior"
maxhp3 = 15
wp3 = 2
maxmp3 = 0
mp3 = 0
ap3 = 2
init3 = 2


#maxhp:maximum life points of character
#wp:weapon attack damage
#mp: magic points
#ap: armor points
#init: initiative fase value for character

#Starting scrren/ main menu
def main():
    os.system('cls') 
    print ("Welcome to Monster Duelists")
    print("1.- Start")
    print("2.- Exit")
    option = input("->")
    if option == "1":
        start()
    elif option == "2":
        sys.exit()
    else:
        main()

#Starting stats displayed to the player before changes 
def start():
    print("Warrior")
    print("Healht:" + str(maxhp))
    print("Attack:" + str(wp))
    print("Magic Points:"+ str(mp))
    print("Priest")
    print("Healht:" + str(maxhp2))
    print("Attack:" + str(wp2))
    print("Magic Points:" + str(mp2))
    print("1.- Fight")
    print("2.- Exit")
    option = input("->")
    if option == "1":
        fight()
    elif option == "2":
        sys.exit()
    else:
        start()

 

#option ex: fight run etc... only fight action is implemented
def fight():
    os.system('cls')
    print("1.- Attack")
    option = input("->")
    if option =="1":
        attack()
    else:
        fight

#attack fase with initiative fase included
def attack():
    os.system('cls')
    name = "warrior"
    maxhp = 32
    wp = 5
    maxmp = 5
    mp = 5
    ap = 2
    init = 2



    name2 = "priest"
    maxhp2 = 20
    wp2 = 2
    maxmp2 = 25
    mp2 = 25
    ap2 = 0
    init2 = 6



    name3 = "orc_warrior"
    maxhp3 = 15
    wp3 = 2
    maxmp3 = 0
    mp3 = 0
    ap3 = 2
    init3 = 2



#cycle to when charaters are alive continue or end the game or make a character unplayable:
    while int(maxhp > 0 or maxhp2 > 0 and maxhp3 >0):
        #initiative fase calculation: 
        wd20 = (random.randint(1, 20))
        pd20 = (random.randint(1, 20))
        od20 = (random.randint(1, 20))

        initiative1 = wd20 + init #warrior initiative
        initiative2= pd20 + init2 #priest initiative
        initiative3= od20 + init3 #orc initiative

        
#Beggining of attack chances and calculation of damage: 
        if int(initiative1 > initiative2 and initiative1 > initiative3 and initiative2>initiative3): #Warrior 1st , priest 2nd and orc 3rd
            if maxhp > 0: #Warrior turn start
                print ("In order the first to attack will be the Warrior followed by the Priest and then the Orc")
                print ("You are controlling the Warrior") 
                playerinput= input("Do you want to a pyshical Attack or a Magic attack?  ")
                if playerinput == "Attack" : 
                    enemy_select= input("Who is your target? "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                    if enemy_select == 'Orc Warrior':
                        dmg = wp - ap3#CalculateDamage
                        print ("Warrior attacks the Orc Warrior "+"\n"+"He dealt "+str(dmg)+" damage to the Orc Warrior")
                        maxhp3 = maxhp3 - dmg#UpdateValues
                        print ("The Orc Warrior has "+str(maxhp3)+" hp left")
                    elif enemy_select == 'Priest':
                        print ("FRIENDLY FIRE!?")
                elif playerinput == 'Magic':
                    print ("You choose Magic")
                    spell_mp_value = 5
                    if mp >= spell_mp_value:
                        spell_select= input("Choose a spell to utilize "+"\n"+"Available spells:"+"\n"+"Warbringer"+"\n"": ")
                        if spell_select == 'Warbringer':
                            enemy_select = input("Choose an enemie to Attack "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                            if enemy_select == 'Orc Warrior':
                                wd4 = (random.randint(1,4))
                                speel_action = -1 * (wp3 + wd4)
                                wp3 = wp3 + speel_action
                                if wp3 < 0 :
                                    wp3 = 0
                                    print ("You used Warbringer on Orc Warrior and now he will do "+str(wp3)+" damage") 
                                else:
                                    pass
                            else:
                                print("You can`t do that!")
                        else:
                            print("You can`t do that!")
                    else:
                        print("You can`t do that!")
                else:
                    print("You can`t do that!") 
            else:
                print ("The Warrior died!")
            pass  #Warrior turn end
            if maxhp2 > 0:     #Priest turn start
                print ("You are controlling the Priest")
                playerinput= input("Do you want to a pyshical Attack or a Magic attack?  ")
                if playerinput == "Attack" : 
                    enemy_select= input("Who is your target? "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                    if enemy_select == 'Orc Warrior':
                        dmg = wp2 - ap3#CalculateDamage
                        print ("The Priest attacks Orc Warrior "+"\n"+"He dealt "+str(dmg)+" damage")
                        maxhp3 = maxhp3 - dmg#UpdateValues
                        print ("Orc Warrior has "+str(maxhp3)+" hp left")
                    elif enemy_select == 'Warrior':
                        print ("FRIENDLY FIRE!?")
                elif playerinput == 'Magic':
                    print ("You choose Magic")
                    spell_mp_value = 5
                    if mp2 >= spell_mp_value:
                        spell_select= input("Choose a spell to utilize "+"\n"+"Available spells:"+"\n"+"Warbringer"+"\n"+"Damage Difusion"+"\n"": ")
                        if spell_select == 'Warbringer':
                            enemy_select = input("Choose an enemie to Attack "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                            if enemy_select == 'Orc Warrior':
                                wd4 = (random.randint(1,4))
                                speel_action = -1 * (wp3 + wd4)
                                wp3 = wp3 + speel_action
                                if wp3 < 0 :
                                    wp3 = 0
                                    print ("You used Warbringer on Orc Warrior and now he will do "+str(wp3)+" damage")
                        elif spell_select == 'Damage Difusion':
                                ChooseTeammate = input ("Choose a teammate to use this spell on "+"\n"+"Avaiable teammates:"+"\n"+"Warrior"+"\n"": ")
                                if ChooseTeammate == 'Warrior':
                                    pd6 = (random.randint(1,6))
                                    speel_action = pd6 + wp2
                                    spell_mp_value = 3
                                    maxhp = maxhp + speel_action
                                    print ("You used Damage Difusion on Warrior and now he has "+str(maxhp)+" hp left")
                                    mp2 = mp2 - spell_mp_value
                                    print ("You used "+str(spell_mp_value)+" MP points and now you have "+str(mp2)+" left")
                                else:
                                    print ("You can not use this spell on "+ChooseTeammate)
                        else:
                            print ("Ths spell doesn't exist")
                    else:
                        print ("You dont have enough MP points to use spells")
                else:
                    print ("That Action doesn't exist")
            else:
                print ("The Priest died!")
            pass  #Priest turn end
            if maxhp3 > 0:  #Orc turn start
                print ("You are now controlling the Orc")

                enemy_select= input("Who is your target? "+"\n"+"Avaiable enemies:"+"\n"+"Warrior"+"\n"+"Priest"+"\n"": ")
                if enemy_select == 'Warrior':
                    dmg = wp3 - ap#CalculateDamage
                    if dmg < 0:
                        dmg = 0
                        maxhp = maxhp - dmg#UpdateValues
                        print ("Orc Warrior attacks the Warrior "+"\n"+"He dealt "+str(dmg)+" damage to the warrior")
                        print ("The warrior has "+str(maxhp)+" hp left")
                    else:
                        maxhp = maxhp - dmg#UpdateValues
                        print ("Orc Warrior attacks the Warrior "+"\n"+"He dealt "+str(dmg)+" damage to the warrior")
                        print ("The warrior has "+str(maxhp)+" hp left")
                elif enemy_select == 'Priest':
                    dmg = wp3 - ap2#CalculateDamage
                    if dmg < 0 :
                        dmg = 0
                        print ("Orc Warrior attacks the Priest"+"\n"+"He dealt "+str(dmg)+" damage to the Priest")
                        maxhp2 = maxhp2 - dmg#UpdateValues
                        print ("The Priest has "+str(maxhp2)+" hp left")
                    else:
                        maxhp2 = maxhp2 - dmg#UpdateValues
                        print ("Orc Warrior attacks the Priest "+"\n"+"He dealt "+str(dmg)+" damage to the Priest")
                        print ("The Priest has "+str(maxhp2)+" hp left")
                else:
                    print ("Can not attack something that's not here")    
            else:
                print ("The Orc is slained, you are saved!")
            pass   #Orc turn end

#Beggining of attack chances and calculation of damage: 
        elif int(initiative1 > initiative2 and initiative1 > initiative3 and initiative3>initiative2): #Warrior 1st, orc 2nd and priest 3rd
            if maxhp > 0:   #Warrior turn start
                print ("In order the first to attack will be the Warrior followed by the Orc and then the Priest")
                print ("You are controlling the Warrior")   
                playerinput= input("Do you want to a pyshical Attack or a Magic attack?  ")
                if playerinput == "Attack" : 
                    enemy_select= input("Who is your target? "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                    if enemy_select == 'Orc Warrior':
                        dmg = wp - ap3#CalculateDamage
                        print ("Warrior attacks the Orc Warrior "+"\n"+"He dealt "+str(dmg)+" damage to the Orc Warrior")
                        maxhp3 = maxhp3 - dmg#UpdateValues
                        print ("The Orc Warrior has "+str(maxhp3)+" hp left")
                    elif enemy_select == 'Priest':
                        print ("FRIENDLY FIRE!?")
                elif playerinput == 'Magic':
                    print ("You choose Magic")
                    spell_mp_value = 5
                    if mp >= spell_mp_value:
                        spell_select= input("Choose a spell to utilize "+"\n"+"Available spells:"+"\n"+"Warbringer"+"\n"": ")
                        if spell_select == 'Warbringer':
                            enemy_select = input("Choose an enemie to Attack "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                            if enemy_select == 'Orc Warrior':
                                wd4 = (random.randint(1,4))
                                speel_action = -1 * (wp3 + wd4)
                                wp3 = wp3 + speel_action
                                if wp3 < 0 :
                                    wp3 = 0
                                    print ("You used Warbringer on Orc Warrior and now he will do "+str(wp3)+" damage") 
                                else:
                                    pass
                            else:
                                print("You can`t do that!")
                        else:
                            print("You can`t do that!")
                    else:
                        print("You can`t do that!")
                else:
                    print("You can`t do that!") 
            else:
                print ("The Warrior died!")
            pass  #Warrior turn end
            if maxhp3 > 0:  #Orc turn start
                print ("You are now controlling the Orc")

                enemy_select= input("Who is your target? "+"\n"+"Avaiable enemies:"+"\n"+"Warrior"+"\n"+"Priest"+"\n"": ")
                if enemy_select == 'Warrior':
                    dmg = wp3 - ap#CalculateDamage
                    if dmg < 0:
                        dmg = 0
                        maxhp = maxhp - dmg#UpdateValues
                        print ("Orc Warrior attacks the Warrior "+"\n"+"He dealt "+str(dmg)+" damage to the warrior")
                        print ("The warrior has "+str(maxhp)+" hp left")
                    else:
                        maxhp = maxhp - dmg#UpdateValues
                        print ("Orc Warrior attacks the Warrior "+"\n"+"He dealt "+str(dmg)+" damage to the warrior")
                        print ("The warrior has "+str(maxhp)+" hp left")
                elif enemy_select == 'Priest':
                    dmg = wp3 - ap2#CalculateDamage
                    if dmg < 0 :
                        dmg = 0
                        print ("Orc Warrior attacks the Priest"+"\n"+"He dealt "+str(dmg)+" damage to the Priest")
                        maxhp2 = maxhp2 - dmg#UpdateValues
                        print ("The Priest has "+str(maxhp2)+" hp left")
                    else:
                        maxhp2 = maxhp2 - dmg#UpdateValues
                        print ("Orc Warrior attacks the Priest "+"\n"+"He dealt "+str(dmg)+" damage to the Priest")
                        print ("The Priest has "+str(maxhp2)+" hp left")
                else:
                    print ("Can not attack something that's not here")    
            else:
                print ("The Orc is slained, you are saved!")
            pass   #Orc turn end

            if maxhp2 > 0:     #Priest turn start
                print ("You are controlling the Priest")
                playerinput= input("Do you want to a pyshical Attack or a Magic attack?  ")
                if playerinput == "Attack" : 
                    enemy_select= input("Who is your target? "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                    if enemy_select == 'Orc Warrior':
                        dmg = wp2 - ap3#CalculateDamage
                        print ("The Priest attacks Orc Warrior "+"\n"+"He dealt "+str(dmg)+" damage")
                        maxhp3 = maxhp3 - dmg#UpdateValues
                        print ("Orc Warrior has "+str(maxhp3)+" hp left")
                    elif enemy_select == 'Warrior':
                        print ("FRIENDLY FIRE!?")
                elif playerinput == 'Magic':
                    print ("You choose Magic")
                    spell_mp_value = 5
                    if mp2 >= spell_mp_value:
                        spell_select= input("Choose a spell to utilize "+"\n"+"Available spells:"+"\n"+"Warbringer"+"\n"+"Damage Difusion"+"\n"": ")
                        if spell_select == 'Warbringer':
                            enemy_select = input("Choose an enemie to Attack "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                            if enemy_select == 'Orc Warrior':
                                wd4 = (random.randint(1,4))
                                speel_action = -1 * (wp3 + wd4)
                                wp3 = wp3 + speel_action
                                if wp3 < 0 :
                                    wp3 = 0
                                    print ("You used Warbringer on Orc Warrior and now he will do "+str(wp3)+" damage")
                        elif spell_select == 'Damage Difusion':
                                ChooseTeammate = input ("Choose a teammate to use this spell on "+"\n"+"Avaiable teammates:"+"\n"+"Warrior"+"\n"": ")
                                if ChooseTeammate == 'Warrior':
                                    pd6 = (random.randint(1,6))
                                    speel_action = pd6 + wp2
                                    spell_mp_value = 3
                                    maxhp = maxhp + speel_action
                                    print ("You used Damage Difusion on Warrior and now he has "+str(maxhp)+" hp left")
                                    mp2 = mp2 - spell_mp_value
                                    print ("You used "+str(spell_mp_value)+" MP points and now you have "+str(mp2)+" left")
                                else:
                                    print ("You can not use this spell on "+ChooseTeammate)
                        else:
                            print ("Ths spell doesn't exist")
                    else:
                        print ("You dont have enough MP points to use spells")
                else:
                    print ("That Action doesn't exist")
            else:
                print ("The Priest died!")
            pass  #Priest turn end

#Beggining of attack chances and calculation of damage: 
        elif int(initiative2 > initiative1 and initiative2 > initiative3 and initiative1>initiative3): #Priest 1st, warrior 2nd and orc 3rd
            if maxhp2 > 0:     #Priest turn start
                print ("So the Priest will play first, the Warrior will be second, and the Orc will be the last")
                print ("You are controlling the Priest")
                playerinput= input("Do you want to a pyshical Attack or a Magic attack?  ")
                if playerinput == "Attack" : 
                    enemy_select= input("Who is your target? "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                    if enemy_select == 'Orc Warrior':
                        dmg = wp2 - ap3#CalculateDamage
                        print ("The Priest attacks Orc Warrior "+"\n"+"He dealt "+str(dmg)+" damage")
                        maxhp3 = maxhp3 - dmg#UpdateValues
                        print ("Orc Warrior has "+str(maxhp3)+" hp left")
                    elif enemy_select == 'Warrior':
                        print ("FRIENDLY FIRE!?")
                elif playerinput == 'Magic':
                    print ("You choose Magic")
                    spell_mp_value = 5
                    if mp2 >= spell_mp_value:
                        spell_select= input("Choose a spell to utilize "+"\n"+"Available spells:"+"\n"+"Warbringer"+"\n"+"Damage Difusion"+"\n"": ")
                        if spell_select == 'Warbringer':
                            enemy_select = input("Choose an enemie to Attack "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                            if enemy_select == 'Orc Warrior':
                                wd4 = (random.randint(1,4))
                                speel_action = -1 * (wp3 + wd4)
                                wp3 = wp3 + speel_action
                                if wp3 < 0 :
                                    wp3 = 0
                                    print ("You used Warbringer on Orc Warrior and now he will do "+str(wp3)+" damage")
                        elif spell_select == 'Damage Difusion':
                                ChooseTeammate = input ("Choose a teammate to use this spell on "+"\n"+"Avaiable teammates:"+"\n"+"Warrior"+"\n"": ")
                                if ChooseTeammate == 'Warrior':
                                    pd6 = (random.randint(1,6))
                                    speel_action = pd6 + wp2
                                    spell_mp_value = 3
                                    maxhp = maxhp + speel_action
                                    print ("You used Damage Difusion on Warrior and now he has "+str(maxhp)+" hp left")
                                    mp2 = mp2 - spell_mp_value
                                    print ("You used "+str(spell_mp_value)+" MP points and now you have "+str(mp2)+" left")
                                else:
                                    print ("You can not use this spell on "+ChooseTeammate)
                        else:
                            print ("Ths spell doesn't exist")
                    else:
                        print ("You dont have enough MP points to use spells")
                else:
                    print ("That Action doesn't exist")
            else:
                print ("The Priest died!")
            pass  #Priest turn end

            if maxhp > 0:
                print ("You are controlling the Warrior")   #Warrior turn start 
                playerinput= input("Do you want to a pyshical Attack or a Magic attack?  ")
                if playerinput == "Attack" : 
                    enemy_select= input("Who is your target? "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                    if enemy_select == 'Orc Warrior':
                        dmg = wp - ap3#CalculateDamage
                        print ("Warrior attacks the Orc Warrior "+"\n"+"He dealt "+str(dmg)+" damage to the Orc Warrior")
                        maxhp3 = maxhp3 - dmg#UpdateValues
                        print ("The Orc Warrior has "+str(maxhp3)+" hp left")
                    elif enemy_select == 'Priest':
                        print ("FRIENDLY FIRE!?")
                elif playerinput == 'Magic':
                    print ("You choose Magic")
                    spell_mp_value = 5
                    if mp >= spell_mp_value:
                        spell_select= input("Choose a spell to utilize "+"\n"+"Available spells:"+"\n"+"Warbringer"+"\n"": ")
                        if spell_select == 'Warbringer':
                            enemy_select = input("Choose an enemie to Attack "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                            if enemy_select == 'Orc Warrior':
                                wd4 = (random.randint(1,4))
                                speel_action = -1 * (wp3 + wd4)
                                wp3 = wp3 + speel_action
                                if wp3 < 0 :
                                    wp3 = 0
                                    print ("You used Warbringer on Orc Warrior and now he will do "+str(wp3)+" damage") 
                                else:
                                    pass
                            else:
                                print("You can`t do that!")
                        else:
                            print("You can`t do that!")
                    else:
                        print("You can`t do that!")
                else:
                    print("You can`t do that!") 
            else:
                print ("The Warrior died!")
            pass  #Warrior turn end

            if maxhp3 > 0:  #Orc turn start
                print ("You are now controlling the Orc")

                enemy_select= input("Who is your target? "+"\n"+"Avaiable enemies:"+"\n"+"Warrior"+"\n"+"Priest"+"\n"": ")
                if enemy_select == 'Warrior':
                    dmg = wp3 - ap#CalculateDamage
                    if dmg < 0:
                        dmg = 0
                        maxhp = maxhp - dmg#UpdateValues
                        print ("Orc Warrior attacks the Warrior "+"\n"+"He dealt "+str(dmg)+" damage to the warrior")
                        print ("The warrior has "+str(maxhp)+" hp left")
                    else:
                        maxhp = maxhp - dmg#UpdateValues
                        print ("Orc Warrior attacks the Warrior "+"\n"+"He dealt "+str(dmg)+" damage to the warrior")
                        print ("The warrior has "+str(maxhp)+" hp left")
                elif enemy_select == 'Priest':
                    dmg = wp3 - ap2#CalculateDamage
                    if dmg < 0 :
                        dmg = 0
                        print ("Orc Warrior attacks the Priest"+"\n"+"He dealt "+str(dmg)+" damage to the Priest")
                        maxhp2 = maxhp2 - dmg#UpdateValues
                        print ("The Priest has "+str(maxhp2)+" hp left")
                    else:
                        maxhp2 = maxhp2 - dmg#UpdateValues
                        print ("Orc Warrior attacks the Priest "+"\n"+"He dealt "+str(dmg)+" damage to the Priest")
                        print ("The Priest has "+str(maxhp2)+" hp left")
                else:
                    print ("Can not attack something that's not here")    
            else:
                print ("The Orc is slained, you are saved!")
            pass   #Orc turn end

#Beggining of attack chances and calculation of damage: 
        elif int(initiative2 > initiative1 and initiative2 > initiative3 and initiative3>initiative1): #priest 1st, orc 2nd and warrior 3rd
            if maxhp2 > 0: #Priest turn start
                print("So the Priest will play first, the Orc will be second, and the Warrior will be the last")
                print ("You are controlling the Priest")
                playerinput= input("Do you want to a pyshical Attack or a Magic attack?  ")
                if playerinput == "Attack" : 
                    enemy_select= input("Who is your target? "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                    if enemy_select == 'Orc Warrior':
                        dmg = wp2 - ap3#CalculateDamage
                        print ("The Priest attacks Orc Warrior "+"\n"+"He dealt "+str(dmg)+" damage")
                        maxhp3 = maxhp3 - dmg#UpdateValues
                        print ("Orc Warrior has "+str(maxhp3)+" hp left")
                    elif enemy_select == 'Warrior':
                        print ("FRIENDLY FIRE!?")
                elif playerinput == 'Magic':
                    print ("You choose Magic")
                    spell_mp_value = 5
                    if mp2 >= spell_mp_value:
                        spell_select= input("Choose a spell to utilize "+"\n"+"Available spells:"+"\n"+"Warbringer"+"\n"+"Damage Difusion"+"\n"": ")
                        if spell_select == 'Warbringer':
                            enemy_select = input("Choose an enemie to Attack "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                            if enemy_select == 'Orc Warrior':
                                wd4 = (random.randint(1,4))
                                speel_action = -1 * (wp3 + wd4)
                                wp3 = wp3 + speel_action
                                if wp3 < 0 :
                                    wp3 = 0
                                    print ("You used Warbringer on Orc Warrior and now he will do "+str(wp3)+" damage")
                        elif spell_select == 'Damage Difusion':
                                ChooseTeammate = input ("Choose a teammate to use this spell on "+"\n"+"Avaiable teammates:"+"\n"+"Warrior"+"\n"": ")
                                if ChooseTeammate == 'Warrior':
                                    pd6 = (random.randint(1,6))
                                    speel_action = pd6 + wp2
                                    spell_mp_value = 3
                                    maxhp = maxhp + speel_action
                                    print ("You used Damage Difusion on Warrior and now he has "+str(maxhp)+" hp left")
                                    mp2 = mp2 - spell_mp_value
                                    print ("You used "+str(spell_mp_value)+" MP points and now you have "+str(mp2)+" left")
                                else:
                                    print ("You can not use this spell on "+ChooseTeammate)
                        else:
                            print ("Ths spell doesn't exist")
                    else:
                        print ("You dont have enough MP points to use spells")
                else:
                    print ("That Action doesn't exist")
            else:
                print ("The Priest died!")
            pass  #Priest turn end

            if maxhp3 > 0:  #Orc turn start 
                print ("You are now controlling the Orc")

                enemy_select= input("Who is your target? "+"\n"+"Avaiable enemies:"+"\n"+"Warrior"+"\n"+"Priest"+"\n"": ")
                if enemy_select == 'Warrior':
                    dmg = wp3 - ap#CalculateDamage
                    if dmg < 0:
                        dmg = 0
                        maxhp = maxhp - dmg#UpdateValues
                        print ("Orc Warrior attacks the Warrior "+"\n"+"He dealt "+str(dmg)+" damage to the warrior")
                        print ("The warrior has "+str(maxhp)+" hp left")
                    else:
                        maxhp = maxhp - dmg#UpdateValues
                        print ("Orc Warrior attacks the Warrior "+"\n"+"He dealt "+str(dmg)+" damage to the warrior")
                        print ("The warrior has "+str(maxhp)+" hp left")
                elif enemy_select == 'Priest':
                    dmg = wp3 - ap2#CalculateDamage
                    if dmg < 0 :
                        dmg = 0
                        print ("Orc Warrior attacks the Priest"+"\n"+"He dealt "+str(dmg)+" damage to the Priest")
                        maxhp2 = maxhp2 - dmg#UpdateValues
                        print ("The Priest has "+str(maxhp2)+" hp left")
                    else:
                        maxhp2 = maxhp2 - dmg#UpdateValues
                        print ("Orc Warrior attacks the Priest "+"\n"+"He dealt "+str(dmg)+" damage to the Priest")
                        print ("The Priest has "+str(maxhp2)+" hp left")
                else:
                    print ("Can not attack something that's not here")    
            else:
                print ("The Orc is slained, you are saved!")
            pass   #Orc turn end

            if maxhp > 0:
                print ("You are controlling the Warrior")   #Warrior turn start
                playerinput= input("Do you want to a pyshical Attack or a Magic attack?  ")
                if playerinput == "Attack" : 
                    enemy_select= input("Who is your target? "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                    if enemy_select == 'Orc Warrior':
                        dmg = wp - ap3#CalculateDamage
                        print ("Warrior attacks the Orc Warrior "+"\n"+"He dealt "+str(dmg)+" damage to the Orc Warrior")
                        maxhp3 = maxhp3 - dmg#UpdateValues
                        print ("The Orc Warrior has "+str(maxhp3)+" hp left")
                    elif enemy_select == 'Priest':
                        print ("FRIENDLY FIRE!?")
                elif playerinput == 'Magic':
                    print ("You choose Magic")
                    spell_mp_value = 5
                    if mp >= spell_mp_value:
                        spell_select= input("Choose a spell to utilize "+"\n"+"Available spells:"+"\n"+"Warbringer"+"\n"": ")
                        if spell_select == 'Warbringer':
                            enemy_select = input("Choose an enemie to Attack "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                            if enemy_select == 'Orc Warrior':
                                wd4 = (random.randint(1,4))
                                speel_action = -1 * (wp3 + wd4)
                                wp3 = wp3 + speel_action
                                if wp3 < 0 :
                                    wp3 = 0
                                    print ("You used Warbringer on Orc Warrior and now he will do "+str(wp3)+" damage") 
                                else:
                                    pass
                            else:
                                print("You can`t do that!")
                        else:
                            print("You can`t do that!")
                    else:
                        print("You can`t do that!")
                else:
                    print("You can`t do that!") 
            else:
                print ("The Warrior died!")
            pass  #Warrior turn end

#Beggining of attack chances and calculation of damage: 
        elif int(initiative3 > initiative1 and initiative3 > initiative2 and initiative1>initiative2): #Orc 1st/Warrior 2nd/Priest 3rd
            if maxhp3 > 0:  #Orc turn start
                print ("So the Orc will play first, the Warrior be second, and the Priest will be the last")
                print ("You are now controlling the Orc")

                enemy_select= input("Who is your target? "+"\n"+"Avaiable enemies:"+"\n"+"Warrior"+"\n"+"Priest"+"\n"": ")
                if enemy_select == 'Warrior':
                    dmg = wp3 - ap#CalculateDamage
                    if dmg < 0:
                        dmg = 0
                        maxhp = maxhp - dmg#UpdateValues
                        print ("Orc Warrior attacks the Warrior "+"\n"+"He dealt "+str(dmg)+" damage to the warrior")
                        print ("The warrior has "+str(maxhp)+" hp left")
                    else:
                        maxhp = maxhp - dmg#UpdateValues
                        print ("Orc Warrior attacks the Warrior "+"\n"+"He dealt "+str(dmg)+" damage to the warrior")
                        print ("The warrior has "+str(maxhp)+" hp left")
                elif enemy_select == 'Priest':
                    dmg = wp3 - ap2#CalculateDamage
                    if dmg < 0 :
                        dmg = 0
                        print ("Orc Warrior attacks the Priest"+"\n"+"He dealt "+str(dmg)+" damage to the Priest")
                        maxhp2 = maxhp2 - dmg#UpdateValues
                        print ("The Priest has "+str(maxhp2)+" hp left")
                    else:
                        maxhp2 = maxhp2 - dmg#UpdateValues
                        print ("Orc Warrior attacks the Priest "+"\n"+"He dealt "+str(dmg)+" damage to the Priest")
                        print ("The Priest has "+str(maxhp2)+" hp left")
                else:
                    print ("Can not attack something that's not here")    
            else:
                print ("The Orc is slained, you are saved!")
            pass   #Orc turn end

            if maxhp > 0:  #Warrior turn start
                print ("You are controlling the Warrior")
                playerinput= input("Do you want to a pyshical Attack or a Magic attack?  ")
                if playerinput == "Attack" : 
                    enemy_select= input("Who is your target? "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                    if enemy_select == 'Orc Warrior':
                        dmg = wp - ap3#CalculateDamage
                        print ("Warrior attacks the Orc Warrior "+"\n"+"He dealt "+str(dmg)+" damage to the Orc Warrior")
                        maxhp3 = maxhp3 - dmg#UpdateValues
                        print ("The Orc Warrior has "+str(maxhp3)+" hp left")
                    elif enemy_select == 'Priest':
                        print ("FRIENDLY FIRE!?")
                elif playerinput == 'Magic':
                    print ("You choose Magic")
                    spell_mp_value = 5
                    if mp >= spell_mp_value:
                        spell_select= input("Choose a spell to utilize "+"\n"+"Available spells:"+"\n"+"Warbringer"+"\n"": ")
                        if spell_select == 'Warbringer':
                            enemy_select = input("Choose an enemie to Attack "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                            if enemy_select == 'Orc Warrior':
                                wd4 = (random.randint(1,4))
                                speel_action = -1 * (wp3 + wd4)
                                wp3 = wp3 + speel_action
                                if wp3 < 0 :
                                    wp3 = 0
                                    print ("You used Warbringer on Orc Warrior and now he will do "+str(wp3)+" damage") 
                                else:
                                    pass
                            else:
                                print("You can`t do that!")
                        else:
                            print("You can`t do that!")
                    else:
                        print("You can`t do that!")
                else:
                    print("You can`t do that!") 
            else:
                print ("The Warrior died!")
            pass  #Warrior turn end

            if maxhp2 > 0:     #Priest turn start
                print ("You are controlling the Priest")
                playerinput= input("Do you want to a pyshical Attack or a Magic attack?  ")
                if playerinput == "Attack" : 
                    enemy_select= input("Who is your target? "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                    if enemy_select == 'Orc Warrior':
                        dmg = wp2 - ap3#CalculateDamage
                        print ("The Priest attacks Orc Warrior "+"\n"+"He dealt "+str(dmg)+" damage")
                        maxhp3 = maxhp3 - dmg#UpdateValues
                        print ("Orc Warrior has "+str(maxhp3)+" hp left")
                    elif enemy_select == 'Warrior':
                        print ("FRIENDLY FIRE!?")
                elif playerinput == 'Magic':
                    print ("You choose Magic")
                    spell_mp_value = 5
                    if mp2 >= spell_mp_value:
                        spell_select= input("Choose a spell to utilize "+"\n"+"Available spells:"+"\n"+"Warbringer"+"\n"+"Damage Difusion"+"\n"": ")
                        if spell_select == 'Warbringer':
                            enemy_select = input("Choose an enemie to Attack "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                            if enemy_select == 'Orc Warrior':
                                wd4 = (random.randint(1,4))
                                speel_action = -1 * (wp3 + wd4)
                                wp3 = wp3 + speel_action
                                if wp3 < 0 :
                                    wp3 = 0
                                    print ("You used Warbringer on Orc Warrior and now he will do "+str(wp3)+" damage")
                        elif spell_select == 'Damage Difusion':
                                ChooseTeammate = input ("Choose a teammate to use this spell on "+"\n"+"Avaiable teammates:"+"\n"+"Warrior"+"\n"": ")
                                if ChooseTeammate == 'Warrior':
                                    pd6 = (random.randint(1,6))
                                    speel_action = pd6 + wp2
                                    spell_mp_value = 3
                                    maxhp = maxhp + speel_action
                                    print ("You used Damage Difusion on Warrior and now he has "+str(maxhp)+" hp left")
                                    mp2 = mp2 - spell_mp_value
                                    print ("You used "+str(spell_mp_value)+" MP points and now you have "+str(mp2)+" left")
                                else:
                                    print ("You can not use this spell on "+ChooseTeammate)
                        else:
                            print ("Ths spell doesn't exist")
                    else:
                        print ("You dont have enough MP points to use spells")
                else:
                    print ("That Action doesn't exist")
            else:
                print ("The Priest died!")
            pass  #Priest turn end

#Beggining of attack chances and calculation of damage: 
        elif int(initiative3 > initiative1 and initiative3 > initiative2 and initiative2>initiative1): #orc 1st, priest 2nd and warrior 3rd
            if maxhp3 > 0:  #Orc turn start
                print ("So the Orc will play first, the Priest be second, and the Warrior will be the last")
                print ("You are now controlling the Orc")

                enemy_select= input("Who is your target? "+"\n"+"Avaiable enemies:"+"\n"+"Warrior"+"\n"+"Priest"+"\n"": ")
                if enemy_select == 'Warrior':
                    dmg = wp3 - ap#CalculateDamage
                    if dmg < 0:
                        dmg = 0
                        maxhp = maxhp - dmg#UpdateValues
                        print ("Orc Warrior attacks the Warrior "+"\n"+"He dealt "+str(dmg)+" damage to the warrior")
                        print ("The warrior has "+str(maxhp)+" hp left")
                    else:
                        maxhp = maxhp - dmg#UpdateValues
                        print ("Orc Warrior attacks the Warrior "+"\n"+"He dealt "+str(dmg)+" damage to the warrior")
                        print ("The warrior has "+str(maxhp)+" hp left")
                elif enemy_select == 'Priest':
                    dmg = wp3 - ap2#CalculateDamage
                    if dmg < 0 :
                        dmg = 0
                        print ("Orc Warrior attacks the Priest"+"\n"+"He dealt "+str(dmg)+" damage to the Priest")
                        maxhp2 = maxhp2 - dmg#UpdateValues
                        print ("The Priest has "+str(maxhp2)+" hp left")
                    else:
                        maxhp2 = maxhp2 - dmg#UpdateValues
                        print ("Orc Warrior attacks the Priest "+"\n"+"He dealt "+str(dmg)+" damage to the Priest")
                        print ("The Priest has "+str(maxhp2)+" hp left")
                else:
                    print ("Can not attack something that's not here")    
            else:
                print ("The Orc is slained, you are saved!")
            pass   #Orc turn end
            if maxhp > 0:
                print ("You are controlling the Warrior")   #Warrior turn start
                playerinput= input("Do you want to a pyshical Attack or a Magic attack?  ")
                if playerinput == "Attack" : 
                    enemy_select= input("Who is your target? "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                    if enemy_select == 'Orc Warrior':
                        dmg = wp - ap3#CalculateDamage
                        print ("Warrior attacks the Orc Warrior "+"\n"+"He dealt "+str(dmg)+" damage to the Orc Warrior")
                        maxhp3 = maxhp3 - dmg#UpdateValues
                        print ("The Orc Warrior has "+str(maxhp3)+" hp left")
                    elif enemy_select == 'Priest':
                        print ("FRIENDLY FIRE!?")
                elif playerinput == 'Magic':
                    print ("You choose Magic")
                    spell_mp_value = 5
                    if mp >= spell_mp_value:
                        spell_select= input("Choose a spell to utilize "+"\n"+"Available spells:"+"\n"+"Warbringer"+"\n"": ")
                        if spell_select == 'Warbringer':
                            enemy_select = input("Choose an enemie to Attack "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                            if enemy_select == 'Orc Warrior':
                                wd4 = (random.randint(1,4))
                                speel_action = -1 * (wp3 + wd4)
                                wp3 = wp3 + speel_action
                                if wp3 < 0 :
                                    wp3 = 0
                                    print ("You used Warbringer on Orc Warrior and now he will do "+str(wp3)+" damage") 
                                else:
                                    pass
                            else:
                                print("You can`t do that!")
                        else:
                            print("You can`t do that!")
                    else:
                        print("You can`t do that!")
                else:
                    print("You can`t do that!") 
            else:
                print ("The Warrior died!")
            pass  #Warrior turn end

            if maxhp2 > 0:     #Priest turn start
                print ("You are controlling the Priest")
                playerinput= input("Do you want to a pyshical Attack or a Magic attack?  ")
                if playerinput == "Attack" : 
                    enemy_select= input("Who is your target? "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                    if enemy_select == 'Orc Warrior':
                        dmg = wp2 - ap3#CalculateDamage
                        print ("The Priest attacks Orc Warrior "+"\n"+"He dealt "+str(dmg)+" damage")
                        maxhp3 = maxhp3 - dmg#UpdateValues
                        print ("Orc Warrior has "+str(maxhp3)+" hp left")
                    elif enemy_select == 'Warrior':
                        print ("FRIENDLY FIRE!?")
                elif playerinput == 'Magic':
                    print ("You choose Magic")
                    spell_mp_value = 5
                    if mp2 >= spell_mp_value:
                        spell_select= input("Choose a spell to utilize "+"\n"+"Available spells:"+"\n"+"Warbringer"+"\n"+"Damage Difusion"+"\n"": ")
                        if spell_select == 'Warbringer':
                            enemy_select = input("Choose an enemie to Attack "+"\n"+"Avaiable enemies:"+"\n"+"Orc Warrior"+"\n"": ")
                            if enemy_select == 'Orc Warrior':
                                wd4 = (random.randint(1,4))
                                speel_action = -1 * (wp3 + wd4)
                                wp3 = wp3 + speel_action
                                if wp3 < 0 :
                                    wp3 = 0
                                    print ("You used Warbringer on Orc Warrior and now he will do "+str(wp3)+" damage")
                        elif spell_select == 'Damage Difusion':
                                ChooseTeammate = input ("Choose a teammate to use this spell on "+"\n"+"Avaiable teammates:"+"\n"+"Warrior"+"\n"": ")
                                if ChooseTeammate == 'Warrior':
                                    pd6 = (random.randint(1,6))
                                    speel_action = pd6 + wp2
                                    spell_mp_value = 3
                                    maxhp = maxhp + speel_action
                                    print ("You used Damage Difusion on Warrior and now he has "+str(maxhp)+" hp left")
                                    mp2 = mp2 - spell_mp_value
                                    print ("You used "+str(spell_mp_value)+" MP points and now you have "+str(mp2)+" left")
                                else:
                                    print ("You can not use this spell on "+ChooseTeammate)
                        else:
                            print ("Ths spell doesn't exist")
                    else:
                        print ("You dont have enough MP points to use spells")
                else:
                    print ("That Action doesn't exist")
            else:
                print ("The Priest died!")
            pass  #Priest turn end
main()

