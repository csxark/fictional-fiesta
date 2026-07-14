class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map={}
        for i,x in enumerate(nums):
            need=target-x
            if need in index_map:
                return index_map[need],i
            index_map[x]=i
        return None