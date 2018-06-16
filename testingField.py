from sys import argv
import math


class creature(object):
    objs = []


    def __init__(obj, posX, posY, tag, hp, hpCup, objWeight, speed):
        obj.posX = posX
        obj.posY = posY
        obj.tag = tag #indicate which type of creature it is

        obj.hp = hp
        obj.hpCup = hpCup
        obj.objWeight = objWeight
        obj.speed = speed #number of rounds a creature need to move a pix, need to be larger than 1, integer

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
            obj.move(1)







class valkyrie(creature):

    def __init__(obj, posX, posY, tag, name, str, dex, con, intl, luk, hp, hpCup, mp, mpCup, attack, defense, dodgeChance, objWeight, movingWeight, speed):
        super(valkyrie, obj).__init__(posX, posY, tag, hp, hpCup, objWeight, speed)

        obj.name = name

        obj.str = str
        obj.dex = dex
        obj.con = con
        obj.intl = intl
        obj.luk = luk

        #equations need fixs
        obj.hp = hp
        obj.hpCup = str/5 + con
        obj.mp = mp
        obj.mpCup = intl * 2
        obj.attack = str + dex * 0.2
        obj.defense = con * 0.5
        obj.dodgeChance = dex #depricated for now

        obj.objWeight = objWeight #can be changed with interactions with facilities
        obj.movingWeight = movingWeight #weight that is used when calculating movement range
        obj.speed = math.floor( 1 + (movingWeight * 2) / objWeight ) #how many turns does it need to make one move, need fix

    def report(obj):
        #print out all sorts of instance information
        e1 = "name = %r " %obj.name
        e2 = "posX = %r " %obj.posX
        e3 = "posY = %r " %obj.posY
        e4 = "hp = %r " %obj.hp

        print e1 + e2 + e3 + e4



class item(object):
    def __init__(obj, posX, posY, name, endurance, rank):
        obj.posX = posX
        obj.posY = posY
        obj.name = name
        obj.endurance = endurance
        obj.rank = rank


class equipment(item):
    def __init__(obj, posX, posY, name, endurance, rank, bodyPart):
        super(item, obj).__init__(posX, posY, name, endurance, rank)
        obj.bodyPart = bodyPart

class weapon(equipment):
    def __init__(obj, posX, posY, name, endurance, rank, bodyPart, attack, defense, parryRate):
        super(equipment, obj).__init__(posX, posY, name, endurance, rank, bodyPart)
        obj.attack = attack
        obj.defense = defense
        obj.parryRate = parryRate


class armor(equipment):
    def __init__(obj, posX, posY, name, endurance, rank, bodyPart, attack, defense, parryRate):
        super(equipment, obj).__init__(posX, posY, name, endurance, rank, bodyPart)
        obj.attack = attack
        obj.defense = defense
        obj.parryRate = parryRate

class spec(equipment):
    #if needed
    pass


class furniture(item):
    pass

class turret(item):
    pass


class building(object):
    pass
class economicStructure(building):
    pass



class map(object):
    pass

class terrain(object):
    pass

class engine(object): #use class list to seprately call ALL instances of ALL classes to perform next-step
    def attack(obj, attacker, defender): #obj arg is always needed when packing a function in a method
        #interactions between objects, put here
        if (attacker.posX == defender.posX and attacker.posY == defender.posY) == 1:
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

gameEngine.attack(valkyrie1,valkyrie2)
gameEngine.move(valkyrie1,1)


#creature1.report()
#creature2.report()
valkyrie1.report()
valkyrie2.report()
