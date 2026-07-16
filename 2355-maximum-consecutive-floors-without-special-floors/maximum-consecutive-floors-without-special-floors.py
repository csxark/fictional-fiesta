class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        first=special[0]-bottom
        last=top-special[-1]
        longest=max(first,last)
        for i in range(len(special)-1):
            gap=special[i+1]-special[i]-1
            longest = max(longest, gap)
        return longest