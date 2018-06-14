from sys import argv
import math


class creature(object):

    def __init__(self, posX, posY, tag, hp, hpCup, selfWeight, speed):
        self.posX = posX
        self.posY = posY
        self.tag = tag #indicate which type of creature it is

        self.hp = hp
        self.hpCup = hpCup
        self.selfWeight = selfWeight
        self.speed = speed #number of rounds a creature need to move a pix, need to be larger than 1, integer


    def move(self, direction):
    #need to add error detection
    # need to add speed algorithm based on game engine
        if direction == 5:
            return "idle"
        elif direction == 1:
            self.posX = self.posX - 1
            self.posY = self.posY - 1
        elif direction == 2:
            self.posY = self.posY - 1
        elif direction == 3:
            self.posX = self.posX + 1
            self.posY = self.posY - 1
        elif direction == 4:
            self.posX = self.posX - 1
        elif direction == 6:
            self.posX = self.posX + 1
        elif direction == 7:
            self.posX = self.posX - 1
            self.posY = self.posY + 1
        elif direction == 8:
            self.posY = self.posY + 1
        elif direction == 9:
            self.posX = self.posX + 1
            self.posY = self.posY + 1

    def report(self):
        print "posX = %r" %self.posX
        print "posY = %r" %self.posY


class valkyrie(creature):

    def __init__(self, posX, posY, tag, name, str, dex, con, intl, luk, hp, hpCup, selfWeight, movingWeight, speed):
        super(valkyrie, self).__init__(posX, posY, tag, hp, hpCup, selfWeight, speed)

        self.name = name

        self.str = str
        self.dex = dex
        self.con = con
        self.intl = intl
        self.luk = luk

        self.hp = hp
        self.hpCup = str/5 + con
        self.selfWeight = selfWeight #can be changed with interactions with facilities
        self.movingWeight = movingWeight #weight that is used when calculating movement range
        self.speed = math.floor( 1 + (movingWeight * 2) / selfWeight ) #how many turns does it need to make one move, need fix





class item(object):
    def __init__(self, posX, posY, name, endurance, rank):
        self.posX = posX
        self.posY = posY
        self.name = name
        self.endurance = endurance
        self.rank = rank


class equipment(item):
    def __init__(self, posX, posY, name, endurance, rank, bodyPart):
        super(item, self).__init__(posX, posY, name, endurance, rank)
        self.bodyPart = bodyPart

class weapon(equipment):
    def __init__(self, posX, posY, name, endurance, rank, bodyPart, attack, defense, parryRate):
        super(equipment, self).__init__(posX, posY, name, endurance, rank, bodyPart)
        self.attack = attack
        self.defense = defense
        self.parryRate = parryRate


class armor(equipment):
    def __init__(self, posX, posY, name, endurance, rank, bodyPart, attack, defense, parryRate):
        super(equipment, self).__init__(posX, posY, name, endurance, rank, bodyPart)
        self.attack = attack
        self.defense = defense
        self.parryRate = parryRate

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
    pass
