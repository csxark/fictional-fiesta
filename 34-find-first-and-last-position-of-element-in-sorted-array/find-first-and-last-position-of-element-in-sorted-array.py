class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first,last=len(nums),len(nums)
        low,high=0,len(nums)-1
        while low<=high:
            mid = low+(high-low)//2
            if nums[mid]>=target:
                first=mid
                high=mid-1
            else:
                low=mid+1
        low,high=0,len(nums)-1
        while low<=high:
            mid = low+(high-low)//2
            if nums[mid]>target:
                last=mid
                high=mid-1
            else:
                low=mid+1

        if first==(len(nums)) or nums[first]!=target:
            return[-1,-1]
        else:
            return [first,last-1]