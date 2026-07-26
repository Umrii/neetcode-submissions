class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix=1
        pre=[1]*len(nums)
        new_num=1

        for i in range(len(nums)):

            pre[i]=prefix*new_num
            prefix=nums[i]
            new_num=pre[i]
        
        postfix=1
        post=[1]*len(nums)
        prev_num=1

        for i in range(len(nums)-1,-1,-1):
            post[i]=postfix*prev_num
            postfix=nums[i]
            prev_num=post[i]
        
        res=[1]*len(nums)
        for i in range(len(nums)):
            res[i]=post[i]*pre[i]

        return res


      