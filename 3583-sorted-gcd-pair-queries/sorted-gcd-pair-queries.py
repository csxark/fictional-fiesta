class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_nums=max(nums)
        max_freq=[0]*(max_nums+1)
        gcd_pair=[0]*(max_nums+1)
        for i in nums:
            max_freq[i]+=1
        for i in range(max_nums,0,-1):
            add=sum(max_freq[i::i])
            gcd_pair[i]=add*(add-1)//2-sum(gcd_pair[i::i])
        gcd_pair=list(accumulate(gcd_pair))
        return [bisect.bisect_right(gcd_pair,q) for q in queries]