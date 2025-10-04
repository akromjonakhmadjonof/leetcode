class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_volume = 0
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            max_volume = max(max_volume, height * width)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_volume