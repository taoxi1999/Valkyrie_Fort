import classes
import weaponInit

############################################################

print "Initializing Engine."
gameEngine = classes.engine()


print "Initializing testing environment."
execfile("weaponInit.py")
execfile("armorInit.py")

print "Generating testors."
Hina = classes.valkyrie(5,5,"valkyrie","Hina",5,5,5,5,5,5,100,50,45,0,0)

print "Initialization Successful!"

############################################################

print "--->Starting Initial Report!"
Hina.report()
print "--->Initial Report Complete!"

############################################################

gameEngine.equip(Strall, Hina)
gameEngine.equip(Excalibur, Hina)
gameEngine.equip(Excalibur, Hina)

############################################################

#Final Report Stage
print "--->Starting Final Report!"
Hina.report()
print "--->Final Report Complete!"
