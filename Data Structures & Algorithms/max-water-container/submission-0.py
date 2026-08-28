class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        
        currentMaxArea = (right - left) * min(heights[left], heights[right])
        print(currentMaxArea)

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            currentMaxArea = max(area, currentMaxArea)
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] <= heights[left]:
                right -= 1
        return currentMaxArea

        