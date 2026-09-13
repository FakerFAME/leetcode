class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            # The area is limited by the shorter line
            current_height = min(height[left], height[right])
            current_width = right - left
            max_water = max(max_water, current_height * current_width)

            # Move the pointer with the smaller height inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water