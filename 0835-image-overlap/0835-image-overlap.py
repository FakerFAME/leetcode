from collections import Counter
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        # Collect coordinates of 1s in both images
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        # Count frequency of each shift vector (r2 - r1, c2 - c1)
        shift_counts = Counter()
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift_counts[(r2 - r1, c2 - c1)] += 1
                
        # The maximum frequency represents the maximum overlap
        return max(shift_counts.values()) if shift_counts else 0