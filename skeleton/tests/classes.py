from sys import argv
from random import randint
import math

class creature(object):
    objs = []

    def __init__(obj, posX, posY, tag, hpCup, objWeight, speed):
        obj.posX = posX
        obj.posY = posY
        obj.tag = tag #indicate which type of creature it is

        obj.hp = hpCup
        obj.hpCup = hpCup
        obj.objWeight = objWeight
        obj.speed = speed #number of rounds a creature need to move a pix, need to be larger than 1, integer

        #inheritants also appear in their mother lists
        creature.objs.append(obj)



    def report(obj):
        #print out all sorts of instance information

        e1 = "tag = %r " %obj.tag
        e2 = "posX = %r " %obj.posX
        e3 = "posY = %r " %obj.posY
        print e1 + e2 + e3


    @classmethod
    def step_all(cls):
        for obj in cls.objs:
            #do something to each instance
            tempEngine = engine()
            Death = tempEngine.deathCheck(obj)
            if Death == True:
                obj.death = True
                print "%r is dead!" %obj.name
                obj.hp = -10 # reserve hp = -1 to cheat death skills
            else: pass

class valkyrie(object):
    objs = []

    def __init__(obj, posX, posY, tag, name, str, dex, con, mag, spr, luk, objWeight, movingWeight, speed):

        obj.posX = posX
        obj.posY = posY

        obj.name = name
        obj.lvl = 1
        obj.death = False

        obj.str = str
        obj.dex = dex
        obj.con = con
        obj.mag = mag
        obj.luk = luk

        #equations need fixs
        obj.hpCup = str * 2 + con * 10
        obj.hp = obj.hpCup
        obj.mpCup = mag * 5 + spr * 5
        obj.mp = obj.mpCup
        obj.attack = str + dex * 0.2
        obj.defense = con * 0.5
        obj.dodgeChance = dex #depricated for now
        obj.parryRate = 0
        obj.parryEfficiency = 0

        obj.objWeight = objWeight #can be changed with interactions with facilities
        obj.movingWeight = movingWeight #weight that is used when calculating movement range
        obj.speed = math.floor( 1 + (movingWeight * 2) / objWeight ) #how many turns does it need to make one move, need fix

        #initialized valkyries are naked!
        obj.eqpLeftHandStat = False
        obj.eqpRightHandStat = False
        obj.eqpHeadStat = False
        obj.eqpBreastStat = False
        obj.eqpArmStat = False
        obj.eqpLegStat = False
        obj.eqpShoeStat = False


        #Append new valkyrie instances to valkyrie.objs[]
        valkyrie.objs.append(obj)

    def report(obj):
        #print out all sorts of instance information
        e1 = "name = %r " %obj.name
        e2 = "posX = %r " %obj.posX
        e3 = "posY = %r " %obj.posY
        e4 = "hp = %r " %obj.hp
        e5 = "mp = %r " %obj.mp
        e6 = "attack = %r " %obj.attack
        e7 = "defense = %r " %obj.defense

        print e1 + e2 + e3 + e4 + e5 + e6 +e7

    @classmethod
    def step_all(cls):
        for obj in cls.objs:
            #do something to each instance
            tempEngine = engine()
            Death = tempEngine.deathCheck(obj)
            if Death == True:
                obj.death = True
                print "%r is dead!" %obj.name
                obj.hp = -10 # reserve hp = -1 to cheat death skills
            else: pass

            #refresh status
            obj.hpCup = str * 2 + con * 10
            obj.mpCup = mag * 5 + spr * 5 #depricated

##################################

class item(object):
    def __init__(obj, posX, posY):
        obj.posX = posX
        obj.posY = posY
        obj.endurance = 100
        obj.owner = 'gaea'

class potion(item):
    def __init__(obj, posX, posY):
        super(potion, obj).__init__(posX, posY)

class hpPotion(potion):
    def __init__(obj, posX, posY):
        super(hpPotion, obj).__init__(posX, posY)

class smallHpPotion(hpPotion):
    def __init__(obj, posX, posY):
        super(smallHpPotion, obj).__init__(posX, posY)
        obj.name = "Small HP Potion"
        obj.rank = 1
        obj.hpRecover = 50

class mediumHpPotion(hpPotion):
    def __init__(obj, posX, posY):
        super(mediumHpPotion, obj).__init__(posX, posY)
        obj.name = "Medium HP Potion"
        obj.rank = 2
        obj.hpRecover = 200

class LargeHpPotion(hpPotion):
    def __init__(obj, posX, posY):
        super(LargeHpPotion, obj).__init__(posX, posY)
        obj.name = "Large HP Potion"
        obj.rank = 3
        obj.hpRecover = 1000

class mpPotion(potion):
    def __init__(obj, posX, posY):
        super(mpPotion, obj).__init__(posX, posY)

class smallMpPotion(mpPotion):
    def __init__(obj, posX, posY):
        super(smallMpPotion, obj).__init__(posX, posY)
        obj.name = "Small HP Potion"
        obj.rank = 1
        obj.mpRecover = 10

class mediumMpPotion(mpPotion):
    def __init__(obj, posX, posY):
        super(mediumMpPotion, obj).__init__(posX, posY)
        obj.name = "Medium HP Potion"
        obj.rank = 2
        obj.mpRecover = 50

class LargeMpPotion(mpPotion):
    def __init__(obj, posX, posY):
        super(LargeMpPotion, obj).__init__(posX, posY)
        obj.name = "Large HP Potion"
        obj.rank = 3
        obj.mpRecover = 100

##################################

class equipment(item):
    def __init__(obj, posX, posY, name, rank):
        super(equipment, obj).__init__(posX, posY)
        obj.name = name
        obj.rank = rank
        obj.usr =  'gaea'

class weapon(equipment):
    def __init__(obj, posX, posY, name, rank, bodyPart, attack, defense, parryRate, parryEfficiency):
        super(weapon, obj).__init__(posX, posY, name, rank)
        obj.bodyPart = bodyPart
        obj.attack = attack
        obj.defense = defense #valid if it is a sword&shield weapon
        obj.parryRate = parryRate #in percentage
        obj.parryEfficiency = parryEfficiency #80 stands for 80%

class armor(equipment):
    def __init__(obj, posX, posY, name, rank, bodyPart, attack, defense, dodgeChance):
        super(armor, obj).__init__(posX, posY, name, rank)
        obj.bodyPart = bodyPart
        obj.attack = attack
        obj.defense = defense
        obj.dodgeChance = dodgeChance

class Accessories(equipment):
    def __init__(obj, posX, posY, name, rank, bodyPart, str, dex, con, mag, spr, luk):
        super(armor, obj).__init__(posX, posY, name, rank, bodyPart)
        obj.str = str
        obj.dex = dex
        obj.con = con
        obj.mag = mag
        obj.spr = spr
        obj.luk = luk

##################################

class building(object):
    pass
class economicStructure(building):
    pass
class militaryStructure(building):
    pass
class torrent(militaryStructure):
    pass
class powerStructure(building):
    pass

##################################

class map(object):
    pass

class terrain(object):
    pass

class engine(object): #use class list to seprately call ALL instances of ALL classes to perform next-step
    def attack(obj, attacker, defender): #obj arg is always needed when packing a function in a method
        if (attacker.posX == defender.posX and attacker.posY == defender.posY) == True:

            RND1 = randint(0,100)
            if RND1 <= defender.parryRate:
                #defender parry success!
                print "Defender parry success!"
                attackFin = (attacker.attack * (100 - defender.parryEfficiency)) / 100 #Avoid 2/5=0 problem
            else: attackFin = attacker.attack

            RND2 = randint(0,100)
            if RND2 <= attacker.parryRate:
                #attacker parry success!
                print "Attacker parry success!"
                defendFin = (defender.attack * (100 - attacker.parryEfficiency)) / 100
            else: defendFin = defender.attack


            if attackFin <= defender.defense:
                defenderSub = 0
            else:
                defenderSub = attackFin - defender.defense


            if defendFin <= attacker.defense:
                attackerSub = 0
            else:
                attackerSub = defendFin - attacker.defense

            defender.hp -= defenderSub
            attacker.hp -= attackerSub

    def move(self, obj, direction):

        #need to add error detection
        #need to add speed algorithm based on game engine
        if direction == 5:
            return "idle"
        elif direction == 1:
            obj.posX = obj.posX - 1
            obj.posY = obj.posY - 1
        elif direction == 2:
            obj.posY = obj.posY - 1
        elif direction == 3:
            obj.posX = obj.posX + 1
            obj.posY = obj.posY - 1
        elif direction == 4:
            obj.posX = obj.posX - 1
        elif direction == 6:
            obj.posX = obj.posX + 1
        elif direction == 7:
            obj.posX = obj.posX - 1
            obj.posY = obj.posY + 1
        elif direction == 8:
            obj.posY = obj.posY + 1
        elif direction == 9:
            obj.posX = obj.posX + 1
            obj.posY = obj.posY + 1

    def equip(obj, equipment, valkyrie):#only applicable to valkyries

        def armorAddStat():
            valkyrie.eqpHeadStat = True
            valkyrie.attack = valkyrie.attack + equipment.attack
            valkyrie.defense = valkyrie.defense + equipment.defense
            valkyrie.dodgeChance = valkyrie.dodgeChance + equipment.dodgeChance
            equipment.owner = valkyrie.name
            equipment.usr = valkyrie.name

        def LHWeaponAddStat():#Left Hand Weapon AddStat
            valkyrie.eqpLeftHandStat = True
            valkyrie.attack += equipment.attack
            valkyrie.defense += equipment.defense
            valkyrie.parryRate += equipment.parryRate
            valkyrie.parryEfficiency += equipment.parryEfficiency

        def RHWeaponAddStat():#Right Hand Weapon AddStat
            valkyrie.eqpRightHandStat = True
            valkyrie.attack += equipment.attack
            valkyrie.defense += equipment.defense
            valkyrie.parryRate += equipment.parryRate
            valkyrie.parryEfficiency += equipment.parryEfficiency

        def THWeaponAddStat():#TwoHanded Weapon AddStat
            valkyrie.eqpLeftHandStat = True
            valkyrie.eqpRightHandStat = True
            valkyrie.attack += equipment.attack
            valkyrie.defense += equipment.defense
            valkyrie.parryRate += equipment.parryRate
            valkyrie.parryEfficiency += equipment.parryEfficiency

        if valkyrie.__class__.__name__ == 'valkyrie':
            #equip armor
            if equipment.__class__.__name__ == 'armor':
                if (equipment.bodyPart == 'Head' and valkyrie.eqpHeadStat == False) == True:
                    armorAddStat()
                elif (equipment.bodyPart == 'Breast' and valkyrie.eqpBreastStat == False) == True:
                    armorAddStat()
                elif (equipment.bodyPart == 'Arm' and valkyrie.eqpArmStat == False) == True:
                    armorAddStat()
                elif (equipment.bodyPart == 'Leg' and valkyrie.eqpLegStat == False) == True:
                    armorAddStat()
                elif (equipment.bodyPart == 'Shoe' and valkyrie.eqpShoeStat == False) == True:
                    armorAddStat()
                else: print "Fail to equip Armor: %r " %equipment.name

            if equipment.__class__.__name__ == 'weapon':
                if (equipment.bodyPart == 'LeftHand' and valkyrie.eqpLeftHandStat == False) == True:
                    LHWeaponAddStat()
                elif (equipment.bodyPart == 'RightHand' and valkyrie.eqpRightHandStat == False) == True:
                    RHWeaponAddStat()
                elif (equipment.bodyPart == 'TwoHanded' and valkyrie.eqpLeftHandStat == False and valkyrie.eqpRightHandStat == False) == True:
                    THWeaponAddStat()
                else: print "Fail to equip Weapon: %r " %equipment.name

            if equipment.__class__.__name__ == 'Accessories':
                valkyrie.str += equipment.str
                valkyrie.dex += equipment.dex
                valkyrie.con += equipment.con
                valkyrie.mag += equipment.mag
                valkyrie.spr += equipment.spr
                valkyrie.luk += equipment.luk

    def useItem(obj, item, valkyrie):
        if item.__class__.__bases__[0].__name__ == "hpPotion":
            valkyrie.hp += item.hpRecover
            if valkyrie.hp >= valkyrie.hpCup:
                valkyrie.hp = valkyrie.hpCup
        if item.__class__.__bases__[0].__name__ == "mpPotion":
            valkyrie.mp += item.mpRecover
            if valkyrie.mp >= valkyrie.mpCup:
                valkyrie.mp = valkyrie.mpCup

    def deathCheck(obj, target):
        if target.hp <= 0:
            return True
        else: return False
