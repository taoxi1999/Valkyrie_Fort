import classes
import weaponInit



print "Initializing Engine."
gameEngine = classes.engine()

print "Initializing testing environment."
execfile("weaponInit.py")
execfile("armorInit.py")


Hina = classes.valkyrie(5,5,"valkyrie","Hina",20,20,20,20,20,20,100,50,45,0,0)
potion1 = classes.smallHpPotion(5, 5)
print "Complete!"


print "--->Starting Initial Report!"
Hina.report()
print "--->Initial Report Complete!"

gameEngine.equip(Strall, Hina)
gameEngine.equip(Excalibur, Hina)
gameEngine.equip(Excalibur, Hina)
gameEngine.useItem(potion1, Hina)

#Final Report Stage
print "--->Starting Final Report!"
Hina.report()
print "--->Final Report Complete!"
