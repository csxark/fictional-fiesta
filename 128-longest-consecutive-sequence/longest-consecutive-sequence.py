class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0: 
            return 0
        longest,st=1,set()
        for i in range(n):
            st.add(nums[i])
        for i in st:
            if i-1 not in st:
                cnt=1
                x=i
                while x+1 in st:
                    x=x+1
                    cnt+=1
                longest=max(longest,cnt)
        return longest