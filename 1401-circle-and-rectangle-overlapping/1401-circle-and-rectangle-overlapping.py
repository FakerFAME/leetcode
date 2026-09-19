class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the closest x coordinate on the rectangle to xCenter
        closest_x = max(x1, min(xCenter, x2))
        
        # Find the closest y coordinate on the rectangle to yCenter
        closest_y = max(y1, min(yCenter, y2))
        
        # Calculate squared distance from circle center to (closest_x, closest_y)
        dist_x = closest_x - xCenter
        dist_y = closest_y - yCenter
        
        return dist_x * dist_x + dist_y * dist_y <= radius * radius