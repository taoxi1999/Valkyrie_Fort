from sys import argv
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
            gameEngine.move(obj,1)





class valkyrie(creature):
    objs = []

    def __init__(obj, posX, posY, tag, name, str, dex, con, intl, luk, hpCup, mpCup, objWeight, movingWeight, speed):
        super(valkyrie, obj).__init__(posX, posY, tag, hpCup, objWeight, speed)

        obj.name = name

        obj.str = str
        obj.dex = dex
        obj.con = con
        obj.intl = intl
        obj.luk = luk

        #equations need fixs
        obj.hp = hpCup
        obj.hpCup = str/5 + con
        obj.mp = mpCup
        obj.mpCup = intl * 2
        obj.attack = str + dex * 0.2
        obj.defense = con * 0.5
        obj.dodgeChance = dex #depricated for now
        obj.parryRate = 0

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
        e5 = "attack = %r " %obj.attack
        e6 = "defense = %r " %obj.defense

        print e1 + e2 + e3 + e4 + e5 + e6

    @classmethod
    def step_all(cls):
        for obj in cls.objs:
            #do something to each instance
            gameEngine.move(obj,1)



class item(object):
    def __init__(obj, posX, posY, name, endurance, rank):
        obj.posX = posX
        obj.posY = posY
        obj.name = name
        obj.endurance = endurance
        obj.rank = rank
        obj.owner = 'gaea'


class equipment(item):
    def __init__(obj, posX, posY, name, endurance, rank, bodyPart):
        super(equipment, obj).__init__(posX, posY, name, endurance, rank)
        obj.bodyPart = bodyPart
        obj.usr =  'gaea'

class weapon(equipment):
    def __init__(obj, posX, posY, name, endurance, rank, bodyPart, attack, defense, parryRate):
        super(weapon, obj).__init__(posX, posY, name, endurance, rank, bodyPart)
        obj.attack = attack
        obj.defense = defense #valid if it is a sword&shield weapon
        obj.parryRate = parryRate


class armor(equipment):
    def __init__(obj, posX, posY, name, endurance, rank, bodyPart, attack, defense, dodgeChance):
        super(armor, obj).__init__(posX, posY, name, endurance, rank, bodyPart)
        obj.attack = attack
        obj.defense = defense
        obj.dodgeChance = dodgeChance

class spec(equipment):
    #if needed
    pass



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



class map(object):
    pass

class terrain(object):
    pass

class engine(object): #use class list to seprately call ALL instances of ALL classes to perform next-step
    def attack(obj, attacker, defender): #obj arg is always needed when packing a function in a method
        #interactions between objects, put here
        if (attacker.posX == defender.posX and attacker.posY == defender.posY) == True:
            if attacker.attack <= defender.defense:
                defenderSub = 0
            else:
                defenderSub = attacker.attack - defender.defense
            if defender.attack <= attacker.defense:
                attackerSub = 0
            else:
                attackerSub = defender.attack - attacker.defense
            defender.hp = defender.hp - defenderSub
            attacker.hp = attacker.hp - attackerSub

    def move(self, obj, direction):
    #need to add error detection
    # need to add speed algorithm based on game engine
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
            valkyrie.attack = valkyrie.attack + equipment.attack
            valkyrie.defense = valkyrie.defense + equipment.defense
            valkyrie.parryRate = valkyrie.parryRate + equipment.parryRate

        def LHWeaponAddStat():#Right Hand Weapon AddStat
            valkyrie.eqpRightHandStat = True
            valkyrie.attack = valkyrie.attack + equipment.attack
            valkyrie.defense = valkyrie.defense + equipment.defense
            valkyrie.parryRate = valkyrie.parryRate + equipment.parryRate

        def THWeaponAddStat():#TwoHanded Weapon AddStat
            valkyrie.eqpLeftHandStat = True
            valkyrie.eqpRightHandStat = True
            valkyrie.attack = valkyrie.attack + equipment.attack
            valkyrie.defense = valkyrie.defense + equipment.defense
            valkyrie.parryRate = valkyrie.parryRate + equipment.parryRate


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

                if equipment.__class__.__name__ == 'weapon':
                    if (equipment.bodyPart == 'LeftHand' and valkyrie.eqpLeftHandStat == False) == True:
                        LHWeaponAddStat()
                    elif (equipment.bodyPart == 'RightHand' and valkyrie.eqpRightHandStat == False) == True:
                        RHWeaponAddStat()
                    elif (equipment.bodyPart == 'TwoHanded' and valkyrie.eqpLeftHandStat == False and valkyrie.eqpRightHandStat == False) == True:
                        THWeaponAddStat()










#tester initialization
creature1 = creature(5,5,"creature1",100,100,50,1)
creature2 = creature(5,5,"creature2",100,100,50,1)
valkyrie1 = valkyrie(5,5,"valkyrie","valkyrie1",5,5,5,5,5,100,100,50,50,0,0,0,45,0,0)
valkyrie2 = valkyrie(5,5,"valkyrie","valkyrie2",5,5,5,5,5,100,100,50,50,0,0,0,45,0,0)
gameEngine = engine()
#tester behavior
#creature1.report()
#creature2.report()
valkyrie1.report()
valkyrie2.report()

#gameEngine.attack(valkyrie1,valkyrie2)
#gameEngine.move(valkyrie1,1)
#valkyrie.step_all()

#creature1.report()
#creature2.report()
valkyrie1.report()
valkyrie2.report()
