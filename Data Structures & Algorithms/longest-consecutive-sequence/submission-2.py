class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        numSort=set(nums)

        for n in nums:

            if (n-1) not in numSort:

                length=0
                while (n+length) in nums:
                    length=length+1
                longest=max(length,longest)
        return longest