class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        NumSet=set(nums)
        longest=0
        for num in nums:
            if num-1 not in NumSet:
                length=0
                while num+length in nums:
                    length=length+1
                longest=max(length,longest)
        return longest


        

      