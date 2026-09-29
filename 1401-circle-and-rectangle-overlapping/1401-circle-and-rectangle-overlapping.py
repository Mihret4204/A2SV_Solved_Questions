class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        cx = max(x1,min(x2,xCenter))
        cy = max(y1,min(y2,yCenter))
        d = (xCenter-cx)**2 + (yCenter-cy)**2
        area = radius**2
        return d<=area
     
