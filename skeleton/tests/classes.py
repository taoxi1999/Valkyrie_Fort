from sys import argv
from random import randint
import math

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

class largeHpPotion(hpPotion):
    def __init__(obj, posX, posY):
        super(largeHpPotion, obj).__init__(posX, posY)
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

class largeMpPotion(mpPotion):
    def __init__(obj, posX, posY):
        super(largeMpPotion, obj).__init__(posX, posY)
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

class accessory(equipment):
    def __init__(obj, posX, posY, name, rank, bodyPart, str, dex, con, mag, spr, luk):
        super(accessory, obj).__init__(posX, posY, name, rank)
        obj.bodyPart = 'AccessorySlot'
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



class engine(object): #use class list to seprately call ALL instances of ALL classes to perform next-step
    def __init__(self):
        self.BlankWeapon = weapon(0,0,'NullWeapon',0,'NullHanded',0,0,0,0)
        self.BlankArmor = armor(0,0,'NullArmor',0,'NullPart',0,0,0)
        self.BlankAccessory = accessory(0,0,'NullAccessory',0,"NullAccSlot",0,0,0,0,0,0)
        self.THHolder = weapon(0,0,'THholder',0,'THholder',0,0,0,0) # TwoHanded Holder : Used to block TwoHanded weapon's null hand

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
        elif direction == 2:
            obj.posY = obj.posY - 1
        elif direction == 4:
            obj.posX = obj.posX - 1
        elif direction == 6:
            obj.posX = obj.posX + 1
        elif direction == 8:
            obj.posY = obj.posY + 1


    def equip(obj, equipment, valkyrie):#only applicable to valkyries
        if valkyrie.__class__.__name__ == 'valkyrie':

            if equipment.__class__.__name__ == 'weapon':
                if (equipment.bodyPart == 'LeftHand' and valkyrie.equipmentSlot[0].name == 'NullWeapon') == True:
                    valkyrie.equipmentSlot[0] = equipment
                elif (equipment.bodyPart == 'RightHand' and valkyrie.equipmentSlot[1].name == 'NullWeapon') == True:
                    valkyrie.equipmentSlot[1] = equipment
                elif (equipment.bodyPart == 'TwoHanded' and valkyrie.equipmentSlot[0].name == 'NullWeapon' and valkyrie.equipmentSlot[1].name == 'NullWeapon') == True:
                    valkyrie.equipmentSlot[0] = equipment
                    tempEngine = engine()
                    valkyrie.equipmentSlot[1] = tempEngine.THHolder
                else: print "Fail to equip Weapon: %r " %equipment.name

            if equipment.__class__.__name__ == 'armor':
                if (equipment.bodyPart == 'Head' and valkyrie.equipmentSlot[2].name == 'NullArmor') == True:
                    valkyrie.equipmentSlot[2] = equipment
                elif (equipment.bodyPart == 'Breast' and valkyrie.equipmentSlot[3].name == 'NullArmor') == True:
                    valkyrie.equipmentSlot[3] = equipment
                elif (equipment.bodyPart == 'Arm' and valkyrie.equipmentSlot[4].name == 'NullArmor') == True:
                    valkyrie.equipmentSlot[4] = equipment
                elif (equipment.bodyPart == 'Leg' and valkyrie.equipmentSlot[5].name == 'NullArmor') == True:
                    valkyrie.equipmentSlot[5] = equipment
                elif (equipment.bodyPart == 'Shoe' and valkyrie.equipmentSlot[6].name == 'NullArmor') == True:
                    valkyrie.equipmentSlot[6] = equipment
                else: print "Fail to equip Armor: %r " %equipment.name

            if equipment.__class__.__name__ == 'Accessory':
                if (equipment.bodyPart == 'AccessorySlot' and valkyrie.equipmentSlot[7].name == 'NullAccessory') == True:
                    valkyrie.equipmentSlot[7] = equipment
                elif (equipment.bodyPart == 'AccessorySlot' and valkyrie.equipmentSlot[8].name == 'NullAccessory') == True:
                    valkyrie.equipmentSlot[8] = equipment
                else: print "Fail to equip Accessory: %r " %equipment.name

            valkyrie.step_all()

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

class map(object):
    pass

class terrain(object):
    pass

##################################

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

    def __init__(obj, posX, posY, tag, name):

        tempEngine = engine()

        obj.equipmentSlot = [0]*9 # LeftHand, RightHand, Head, Breast, Arm, Leg, Shoe, Acc1, Acc2
        obj.inventory = []
        obj.equipmentSlot[0] = tempEngine.BlankWeapon
        obj.equipmentSlot[1] = tempEngine.BlankWeapon
        obj.equipmentSlot[2] = tempEngine.BlankArmor
        obj.equipmentSlot[3] = tempEngine.BlankArmor
        obj.equipmentSlot[4] = tempEngine.BlankArmor
        obj.equipmentSlot[5] = tempEngine.BlankArmor
        obj.equipmentSlot[6] = tempEngine.BlankArmor
        obj.equipmentSlot[7] = tempEngine.BlankAccessory
        obj.equipmentSlot[8] = tempEngine.BlankAccessory

        obj.posX = posX
        obj.posY = posY

        obj.name = name
        obj.lvl = 1
        obj.Exp = 0
        obj.lvlUpExp = 500 * obj.lvl
        obj.death = False

        #base points which is only related to lvl
        obj.strBase = obj.lvl * 2
        obj.dexBase = obj.lvl * 2
        obj.conBase = obj.lvl * 2
        obj.magBase = obj.lvl * 2
        obj.sprBase = obj.lvl * 2
        obj.lukBase = obj.lvl * 2

        #Player added points
        obj.strAdd = 0
        obj.dexAdd = 0
        obj.conAdd = 0
        obj.magAdd = 0
        obj.sprAdd = 0
        obj.lukAdd = 0
        obj.allPoints = obj.lvl * 5
        obj.spentPoints  = obj.strAdd + obj.dexAdd + obj.conAdd + obj.magAdd + obj.sprAdd + obj.lukAdd
        obj.freePoints = obj.allPoints - obj.spentPoints

        #Calculated final points
        obj.str = obj.strBase + obj.strAdd + obj.equipmentSlot[7].str + obj.equipmentSlot[8].str
        obj.dex = obj.dexBase + obj.dexAdd + obj.equipmentSlot[7].str + obj.equipmentSlot[8].dex
        obj.con = obj.conBase + obj.conAdd + obj.equipmentSlot[7].str + obj.equipmentSlot[8].con
        obj.mag = obj.magBase + obj.magAdd + obj.equipmentSlot[7].str + obj.equipmentSlot[8].mag
        obj.spr = obj.sprBase + obj.sprAdd + obj.equipmentSlot[7].str + obj.equipmentSlot[8].spr
        obj.luk = obj.lukBase + obj.lukAdd + obj.equipmentSlot[7].str + obj.equipmentSlot[8].luk

        #equations need fixs
        obj.hpCup = obj.str * 2 + obj.con * 10
        obj.hp = obj.hpCup
        obj.mpCup = obj.mag * 5 + obj.spr * 5
        obj.mp = obj.mpCup
        obj.attack = obj.str + obj.dex * 0.2
        obj.defense = obj.con * 0.5
        obj.dodgeChance = obj.dex #depricated for now, encourage dex/con tradeoff
        obj.parryRate = 0 #should have str and con fixture besides weapon attributes
        obj.parryEfficiency = 0 #should have str and con fixture besides weapon attributes

        obj.selfWeight = obj.con #can be changed with interactions with facilities
        obj.carryWeight = obj.con #should be the weight of inventory
        obj.speed = math.floor( 1 + (obj.selfWeight * 2) / obj.carryWeight ) #how many turns does it need to make one move, need fix



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
        e8 = "parryRate = %r " %obj.parryRate

        print e1 + e2 + e3 + e4 + e5 + e6 + e7 + e8
        #print obj.equipmentSlot

    def inventoryCheck(obj): # refresh obj.invList
        obj.invList = [[0,0]] # eg. [["Apple",2],["Stick",5]...]

        for x in obj.inventory:
            count = 0
            for y in obj.invList:
                if x.__class__.__name__ == y[0]:
                    count = y[1] + 1
                else: count = 0
            if count == 0:
                tuple = [x.__class__.__name__,1]
                obj.invList.append(tuple)
            elif count >= 1:
                for z in obj.invList:
                    if x.__class__.__name__ == z[0]:
                        z[1] = count

    def obtain(obj, item):
        obj.inventory.append(item)
        obj.inventoryCheck()

    def drop(obj, itemName):
        pass #drop an item (specific item)
        for x in obj.inventory:
            if x.__class__.__name__ == itemName:
                obj.inventory.remove(x)
                break
            else: print "Nothing to drop."
        obj.inventoryCheck()


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
            #status related to lvl and points added
            obj.str = obj.strBase + obj.strAdd + obj.equipmentSlot[7].str + obj.equipmentSlot[8].str
            obj.dex = obj.dexBase + obj.dexAdd + obj.equipmentSlot[7].str + obj.equipmentSlot[8].dex
            obj.con = obj.conBase + obj.conAdd + obj.equipmentSlot[7].str + obj.equipmentSlot[8].con
            obj.mag = obj.magBase + obj.magAdd + obj.equipmentSlot[7].str + obj.equipmentSlot[8].mag
            obj.spr = obj.sprBase + obj.sprAdd + obj.equipmentSlot[7].str + obj.equipmentSlot[8].spr
            obj.luk = obj.lukBase + obj.lukAdd + obj.equipmentSlot[7].str + obj.equipmentSlot[8].luk

            #equations need fixs
            obj.hpCup = obj.str * 2 + obj.con * 10
            obj.mpCup = obj.mag * 5 + obj.spr * 5
            obj.attack = (obj.str + obj.dex * 0.2) + obj.equipmentSlot[0].attack + obj.equipmentSlot[1].attack
            obj.defense = (obj.con * 0.5) + + obj.equipmentSlot[0].defense + obj.equipmentSlot[1].defense
            obj.dodgeChance = obj.dex #depricated for now, encourage dex/con tradeoff
            obj.parryRate = 0 + obj.equipmentSlot[0].parryRate + obj.equipmentSlot[1].parryRate #should have str and con fixture besides weapon attributes
            obj.parryEfficiency = 0 #should have str and con fixture besides weapon attributes
