class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0 

        l = 0
        r = len(heights) - 1

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])

            temp = width * height

            area = max(area, temp)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return area    