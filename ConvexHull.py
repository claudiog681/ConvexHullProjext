class Points: #Object which stores x and y coordinates
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def get_x(self):
            return self.x
        def get_y(self):
            return self.y


def left_most(point_list): #finds the starting point at the left most point

    min_val = 0
    for i in range(1, len(point_list)): #traverse input array of Points
        if point_list[i].x < point_list[min_val].x:
            min_val = i
        elif point_list[i].x == point_list[min_val].x: #If 2 left most x values set highest y coordiante point
            if point_list[i].y > point_list[min_val].y:
                min_val = i
    return min_val

def slope_function(point1, nextPoint, testPoints):
    # inputs are of Points object
    # use expresion ax+by=c to find relative positions of testPoints
    cExpression = (nextPoint.y - point1.y) * (testPoints.x - nextPoint.x) - (nextPoint.x - point1.x) * (
                testPoints.y - nextPoint.y)

    if cExpression >= 0:  # Points lie on the same line or clockwise position
        return False
    else:  # Points in a counter clockwise position
        return True

def convexHull(point_list, size):
    #Minimum size 3 uses helper methods to create result list in counter clockwise order starting from leftmost point
    in_list = toPointList(point_list)

    if size < 3:
        return in_list
    firstL = left_most(in_list) #get first point
    result = []
    currentP = firstL
    nextQ = 0
    while True:
        result.append(in_list[currentP]) #append current point to hull
        nextQ = (currentP + 1) % size
        for i in range(size): # test current and next point with all points
            if slope_function(in_list[currentP], in_list[i], in_list[nextQ]): # if next point is in the hull
                nextQ = i

        currentP = nextQ
        if currentP == firstL: #end case if the current point is the first point
            break

    #still need to work on getting output to 2d array
    result_list = to2DList(result)
    return result_list

def to2DList(pointsList): #takes list of Points objects and creates a 2D list to save x and y coordinates
    size = len(pointsList)
    rows = size
    cols = 2
    arr = [] #array to save rows and columns
    for i in range(rows):
        col = []
        for j in range(cols):
            if j % 2 == 0: #append x values to first position of each array
                col.append(pointsList[i].x)
            else: #append y values to second position of each array
                col.append(pointsList[i].y)
        arr.append(col)
    return arr

def toPointList(twoDList): #takes 2D list and returns a list of Points objects
    pointList = []
    for i in range(len(twoDList)):
        x = 0
        y = 0
        for j in range(len(twoDList[i])):
            if j % 2 == 0:
                x = twoDList[i][j]
            else:
                y = twoDList[i][j]
        point = Points(x, y)
        pointList.append(point)

    return pointList


# Test Code
'''row = 5
colNum = 2

arr = []
for i in range(5):
    col = []
    for j in range(2):
        col.append(0)
    arr.append(col)
print(arr)'''


points = []

points.append(Points(-3, 1))
points.append(Points(-2, 2))
points.append(Points(1, 3))

'''test = to2DList(points)
test1 = toPointList(test)

for i in range(len(test1)):
    point = test1[i]
    x = point.get_x()
    y = point.get_y()
    print("(" + str(x) + "," + str(y) + ")")'''
#print(test1)
#points.append(Points(2, 1))
#points.append(Points(5, 0))
#points.append(Points(-1, -2))
#points.append(Points(3, 3))

outList = convexHull(to2DList(points), len(points))

for i in range(len(outList)):
    print("(" + str(outList[i][0]) + " , " + str(outList[i][1]) + ")")