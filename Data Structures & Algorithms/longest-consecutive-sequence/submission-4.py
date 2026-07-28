class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        NumSet=set()

        NumSet.add(tuple(nums))
        length=1
        longest=0
        for num in nums:
            if num-1 not in NumSet:
                length=1
                while num+length in nums:
                    length=length+1
                longest=max(length,longest)
        return longest


        

      