class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        low,high,ans=min(nums),max(nums),[]
        for i in range(low,high):
            if i not in nums:
                ans.append(i)
        return ans