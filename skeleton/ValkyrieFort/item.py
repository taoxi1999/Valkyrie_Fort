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

