class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp=0
        for i in range(len(digits)):
            temp=temp*10+digits[i]
        temp+=1
        return  [int(digit) for digit in str(temp)]