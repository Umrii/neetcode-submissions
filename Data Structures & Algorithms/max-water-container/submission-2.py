class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left=0
        right=len(heights)-1
        max_volume=0

        while left<right:

            distance= right-left
            print(left,right)

            min_height=min(heights[left],heights[right])
            volume=distance*min_height
            max_volume=max(volume,max_volume)
            if heights[left]<heights[right]:
                left=left+1
            else:
                right=right-1
        return max_volume




        