import numpy as np
import sys

def createArray():
    inPath = sys.argv[1]
    with open(inPath, 'r') as f:
        line = f.readline().split()
        w = int(line[0])
        h = int(line[1])
    
    mapArray = np.loadtxt(inPath, skiprows=1, dtype=int)
    
    return w, h, mapArray

def computePath(mapArray):
    w = mapArray.shape[1]
    h = mapArray.shape[0]

    for y in range(h):
        for x in range(w):
            computePathOnNode(mapArray, y, x)
    return       

def computePathOnNode(mapArray, y, x):
    maxLen = 1
    maxDepth = 0
    # Find the next value in neighbours
    for [ty, tx] in [[y-1, x], [y, x-1], [y+1, x], [y, x+1]]:
        if ty < 0 or tx < 0 or ty >= mapArray.shape[0] or tx >= mapArray.shape[1]:
            continue
        if mapArray[ty, tx] >= mapArray[y, x]:
            continue
        
        thisNbrLen = computePathOnNode(mapArray, ty, tx)
        
        if maxLen <= 1 + thisNbrLen:
            if maxDepth <= (mapArray[y, x] - mapArray[ty, tx]) + maxDepthArray[ty, tx]:
                maxLen = 1 + thisNbrLen
                maxLenArray[y, x] = maxLen
                maxDepth = (mapArray[y, x] - mapArray[ty, tx]) + maxDepthArray[ty, tx]
                maxDepthArray[y, x] = maxDepth
                nextLocation[y, x] = (ty - y + 2) * 10 + (tx - x + 2)
                
    return maxLen
    
def printValue(mapArray, y, x):
    print '[%d]'%(mapArray[y, x])
    offset = nextLocation[y, x]
    if offset != 0:
        print '|'
        ty = y + offset / 10 - 2
        tx = x + offset % 10 - 2
        printValue(mapArray, ty, tx)
    return
      
if __name__ == '__main__':
    w, h, mapArray = createArray()
    
    global maxLenArray
    maxLenArray = np.ones((h, w), dtype=int)
    global maxDepthArray
    maxDepthArray = np.zeros((h, w), dtype=int)
    global nextLocation
    nextLocation = np.zeros((h, w), dtype=int)
    
    computePath(mapArray)
    
    print '***************************'
    print 'Information of the input:'
    print '***************************'
    print 'w = ' + str(w) + ' h = ' + str(h)  
    print 'MAX = ' + str(np.amax(mapArray)) + ' MIN = ' + str(np.amin(mapArray))

    print '***************************'
    print 'Maximum length and depth of feasible paths:'
    print '***************************'
    maxLen = np.amax(maxLenArray)
    print 'Length = ' + str(maxLen)
    locy, locx = np.where(maxLenArray == maxLen)
    depthList = []
    for i in range(locy.shape[0]):
        depthList.append(maxDepthArray[locy[i], locx[i]])
        
    print 'Depth = ' + str(max(depthList))

    print '***************************'
    print 'Printing the path:'
    print '***************************'    
    nMax = depthList.index(max(depthList))
    printValue(mapArray, locy[nMax], locx[nMax])
