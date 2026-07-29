class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)

        
        
        result=[]
        for i in range(len(nums)):

            if i>0 and nums[i]==nums[i-1]:
                continue
            
            left=i+1
            right=len(nums)-1
            
            while left<right:
                
                
                total=nums[left]+nums[i]+nums[right]
                if total==0:
            
                    result.append([nums[left],nums[i],nums[right]])
                    left=left+1
                    while nums[left]==nums[left-1] and left<right:
                        left=left+1
                if total<0:
                    left=left+1
                if total>0:
                    right=right-1

        return result