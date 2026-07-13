class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result=[]
        for i in range(1,10):
            temp=0
            for j in range(i,10):
                temp=temp*10+j
                if temp>=low and temp<=high:
                    result.append(temp)
        result.sort()
        return result
            