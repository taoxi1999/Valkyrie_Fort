import numpy

#tem = numpy.zeros((10,10))
#tem[0,0]
xSize = 10
ySize = 10

tem = numpy.arange(xSize*ySize).reshape(xSize,ySize)

for x in range(0,xSize):
    for y in range(0,ySize):
        tem[x,y] = 0


print tem



#asset matcher
#list all instance to dictionary

assetMatch = {}



#asset printer
#display correspoding image to instances
#need to match all instances of the same class to the same image
