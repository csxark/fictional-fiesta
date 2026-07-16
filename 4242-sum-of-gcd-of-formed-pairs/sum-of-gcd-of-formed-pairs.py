import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd=[0]*(len(nums))
        max_i=0
        ans=0
        for i in range(len(nums)):
            max_i=max(max_i,nums[i])
            prefixGcd[i]=math.gcd(nums[i],max_i)
        prefixGcd.sort()
        left,right=0,len(prefixGcd)-1
        while left<right:
            ans+=math.gcd(prefixGcd[left],prefixGcd[right])
            left+=1
            right-=1
        return ans

