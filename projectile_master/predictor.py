import point
import math

# projectile_motion-master/predictor.py


class predictor:
    
    def __init__(self):
        self.screenWidth = 1280
        self.screenHeight = 720
        self.path = []
        self.projected = []
        self.horizontalA = 0
        self.verticalA = 10
        self.g = 100000

    def addPointPath(self, p):
        self.path.append(p)

    def distance(self, p1, p2):
        # Calculate the distance between two points
        startX = p1.x
        startY = p1.y
        endX = p2.x
        endY = p2.y

        dX = endX - startX
        dY = endY - startY
        return math.sqrt(pow(dX, 2) + pow(dY, 2))

    def dX(self, p1, p2):
        # Calculate the change in X coordinate between two points
        start = p1.x
        end = p2.x
        return end - start

    def dY(self, p1, p2):
        # Calculate the change in Y coordinate between two points
        start = p1.y
        end = p2.y
        return end - start

    def velocity(self, p1, p2):
        # Calculate the velocity between two points
        return self.distance(p1, p2)

    def velocityX(self, p1, p2):
        # Calculate the velocity in the X direction between two points
        return self.dX(p1, p2)

    def velocityY(self, p1, p2):
        # Calculate the velocity in the Y direction between two points
        return self.dY(p1, p2)

    def nextX(self, p1, p2):
        # Calculate the next X coordinate based on the current point and velocity
        return p2.x + (self.dX(p1, p2) + self.horizontalA)

    def nextY(self, p1, p2):
        # Calculate the next Y coordinate based on the current point and velocity
        vStart = self.dY(p1, p2)
        print(vStart + self.verticalA)
        return p2.y + (vStart + self.verticalA)

    def detectHA(self, p1, p2, p3):
        # Detect the horizontal acceleration based on three points
        start = p1.x
        mid = p2.x
        end = p3.x
        d1 = mid - start
        d2 = end - mid
        dd = d2 - d1
        return dd

    def detectVA(self, p1, p2, p3):
        # Detect the vertical acceleration based on three points
        start = p1.y
        mid = p2.y
        end = p3.y
        d1 = mid - start
        d2 = end - mid
        print(d2 - d1)
        return d2 - d1
        

    class Predictor:
        def projectPath(self):
            """
            Project the path based on the given points.

            This method calculates the projected path of the ball based on the given points.
            It uses the detectHA and detectVA methods to determine the horizontal and vertical angles.
            The projected path is stored in the 'projected' list.

            Returns:
                None
            """
            self.projected = []
            p1 = self.path[-3]
            p2 = self.path[-2]
            p3 = self.path[-1]
            self.horizontalA = self.detectHA(p1, p2, p3)
            self.verticalA = self.detectVA(p1, p2, p3)

            while (p2.x > 0 and p2.x < self.screenWidth) and (p2.y > 0 and p2.y < self.screenHeight):
                newX = int(self.nextX(p1, p2))
                newY = int(self.nextY(p1, p2))
                p1 = p2
                p2 = point(newX, newY)
                print(p2)
                self.projected.append(point(newX, newY))
