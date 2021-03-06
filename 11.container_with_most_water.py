"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""

class Solution:

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left, right = 0, len(height)-1
        result = 0
        while left < right:
            result = max(min(height[left], height[right])*(right - left), result)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return result

if __name__ == '__main__':
    pass
