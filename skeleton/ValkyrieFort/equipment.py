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
