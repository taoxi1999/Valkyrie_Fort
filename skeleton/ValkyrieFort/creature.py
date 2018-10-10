from sys import argv
from random import randint
import math

class creature(object):
    objs = []

    def __init__(self, obj, posX, posY, tag, hpCup, objWeight, speed):
        obj.posX = posX
        obj.posY = posY
        obj.tag = tag #indicate which type of creature it is

        obj.hp = hpCup
        obj.hpCup = hpCup
        obj.objWeight = objWeight
        obj.speed = speed #number of rounds a creature need to move a pix, need to be larger than 1, integer

        #inheritants also appear in their mother lists
        creature.objs.append(obj)



    def report(self):
        #print out all sorts of instance information

        e1 = "tag = %r " %self.tag
        e2 = "posX = %r " %self.posX
        e3 = "posY = %r " %self.posY
        print(e1 + e2 + e3)


    @classmethod
    def step_all(cls):
        for obj in cls.objs:
            #do something to each instance
            tempEngine = engine()
            Death = tempEngine.deathCheck(obj)
            if Death == True:
                obj.death = True
                print("%r is dead!" %obj.name)
                obj.hp = -10 # reserve hp = -1 to cheat death skills
            else: pass