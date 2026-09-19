class Solution:
    def maxArea(self, heights: List[int]) -> int:
        min1 = 0
        max1 = len(heights) - 1
        best = 0

        while min1 < max1:
            area = (max1 - min1) * min(heights[min1], heights[max1])
            if area>best:
                best=area
            if heights[min1] < heights[max1]:
                min1 += 1
            else:
                 max1 -= 1
    

    
        return best     



        