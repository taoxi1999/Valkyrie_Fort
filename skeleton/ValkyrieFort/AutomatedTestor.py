import classes
import weaponInit
import os



print "Initializing Engine."
gameEngine = classes.engine()

print "Initializing testing environment."
execfile("weaponInit.py")
execfile("armorInit.py")
execfile("accessoryInit.py")


Hina = classes.valkyrie(5,5,"valkyrie","Hina")
Gasha = classes.valkyrie(5,5,"valkyrie","Gasha")
potion1 = classes.largeHpPotion(5, 5)
potion2 = classes.smallMpPotion(5, 5)
print "Complete!"


print "--------->Starting Initial Report!"
Hina.report()
Gasha.report()
print "--------->Initial Report Complete!"


Hina.obtain(potion1)
Hina.obtain(potion1)
Hina.obtain(potion2)
Hina.obtain(potion2)

Hina.attack_Act(Gasha)
Hina.useItem(potion1)

print Hina.invList
Hina.drop("smallHpPotion")
print Hina.invList

#Final Report Stage
print "--------->Starting Final Report!"
Hina.report()
Gasha.report()
print "--------->Final Report Complete!"

os.system('rm *.pyc')
