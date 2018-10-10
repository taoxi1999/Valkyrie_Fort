import equipment


class engine(object): #use class list to seprately call ALL instances of ALL classes to perform next-step
    def __init__(self):
        self.BlankWeapon = equipment.weapon(0,0,'NullWeapon',0,'NullHanded',0,0,0,0)
        self.BlankArmor = equipment.armor(0,0,'NullArmor',0,'NullPart',0,0,0)
        self.BlankAccessory = equipment.accessory(0,0,'NullAccessory',0,"NullAccSlot",0,0,0,0,0,0)
        self.THHolder = equipment.weapon(0,0,'THholder',0,'THholder',0,0,0,0) # TwoHanded Holder : Used to block TwoHanded weapon's null hand

    def deathCheck(self, target):
        if target.hp <= 0:
            return True
        else: return False

    def spawnTerrain(self):
        pass

    def refreshTerrain(self):
        pass
