class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left=0
        right=len(nums)-1

        while left<=right:

            mid=(right+left)//2

            if target == nums[mid]:
                return mid

            # here we need to check which part of the sorted array are we in
            # are we in the left sorted array or the right sorted array
            # and we can check that by seeing if nums[mid] is less than or equal
            # to the nums[left]
            if nums[left]<=nums[mid]:
                if target<nums[left] or target > nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
                
            else:

                if target>nums[right] or target < nums[mid]:

                    right=mid-1
                else:
                    left=mid+1

        return -1