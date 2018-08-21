import random

arg = []

for i in range(0,200):
    inst = random.randint(0,3)
    arg.append(inst)






####



def outOf(instance,list):
    result = 0
    for x in list:
        if instance == x:
            result += 1
        else: pass

    if result == 0:
        return True
    else: return False



objList = []
for x in arg:
    if outOf(x,objList)==True:
        objList.append(x)
    else: pass

print objList
