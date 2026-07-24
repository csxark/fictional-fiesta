class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        nums=list(dict.fromkeys(nums))
        ans,temp=set(),set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                temp.add(nums[i]^nums[j])
        for i in temp:
            for j in nums:
                ans.add(i^j)
        return len(ans)
            