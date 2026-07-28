class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        j=n-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==val:
                nums[i],nums[j]=nums[j],nums[i]
                j-=1
                nums.pop()
        
        