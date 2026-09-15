class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        max_dist = 0
        
        # Compare house 0 with houses from right to left
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                max_dist = max(max_dist, i)
                break
                
        # Compare house n-1 with houses from left to right
        for i in range(n):
            if colors[i] != colors[-1]:
                max_dist = max(max_dist, (n - 1) - i)
                break
                
        return max_dist