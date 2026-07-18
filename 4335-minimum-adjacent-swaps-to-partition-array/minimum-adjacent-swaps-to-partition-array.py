class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        mod = 10**9 + 7
        mb, rb, ans = 0, 0, 0
        for x in nums:
            if x < a:
                ans += mb + rb
            elif x <= b:
                ans += rb
                mb += 1
            else:
                rb += 1
        return ans % mod
