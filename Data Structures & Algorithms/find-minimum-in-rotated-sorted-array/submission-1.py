class Solution:
    def findMin(self, nums: List[int]) -> int:

        minimum=nums[0]
        for n in nums:
            minimum=min(n,minimum)

        return minimum
        