class Solution:
    def findMin(self, nums: List[int]) -> int:
        low,high,ans=0,len(nums)-1,nums[0]
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]>=nums[0]:
                low=mid+1
            else:
                ans=nums[mid]
                high=mid-1
        return ans

