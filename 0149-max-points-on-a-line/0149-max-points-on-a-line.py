from collections import defaultdict
import math

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        max_points = 0
        
        for i in range(n):
            slopes = defaultdict(int)
            duplicates = 1
            local_max = 0
            
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                if x1 == x2 and y1 == y2:
                    duplicates += 1
                    continue
                
                dx = x2 - x1
                dy = y2 - y1
                
                # Reduce the slope using GCD to handle signs and precision cleanly
                g = math.gcd(dx, dy)
                dx //= g
                dy //= g
                
                # Normalize negative directions
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                
                slopes[(dx, dy)] += 1
                local_max = max(local_max, slopes[(dx, dy)])
                
            max_points = max(max_points, local_max + duplicates)
            
        return max_points