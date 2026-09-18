class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # Check both X-axis and Y-axis 1D interval overlaps
        overlap_x = rec1[0] < rec2[2] and rec2[0] < rec1[2]
        overlap_y = rec1[1] < rec2[3] and rec2[1] < rec1[3]
        
        return overlap_x and overlap_y