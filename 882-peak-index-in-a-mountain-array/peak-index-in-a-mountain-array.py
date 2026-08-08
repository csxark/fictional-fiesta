class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        if max(nums)==nums[-1]:
            return len(nums)-1
        low,high=0,len(nums)-1
        while low<high:
            mid=low+(high-low)//2
            if nums[mid]<nums[mid+1]:
                low=mid+1
            else:
                high=mid
        return low