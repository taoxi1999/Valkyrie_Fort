import classes
import weaponInit



print "Initializing Engine."
gameEngine = classes.engine()

print "Initializing testing environment."
execfile("weaponInit.py")
execfile("armorInit.py")


Hina = classes.valkyrie(5,5,"valkyrie","Hina",20,20,20,20,20,20,45,0,0)
Gasha = classes.valkyrie(5,5,"valkyrie","Gasha",20,20,20,20,20,20,45,0,0)
potion1 = classes.LargeMpPotion(5, 5)
print "Complete!"


print "--->Starting Initial Report!"
Hina.report()
Gasha.report()
print "--->Initial Report Complete!"

#gameEngine.equip(Strall, Hina)
gameEngine.equip(Excalibur, Hina)
gameEngine.equip(Excalibur, Gasha)
gameEngine.useItem(potion1, Hina)
gameEngine.attack(Hina, Gasha)

classes.valkyrie.step_all()

#Final Report Stage
print "--->Starting Final Report!"
Hina.report()
Gasha.report()
print "--->Final Report Complete!"
