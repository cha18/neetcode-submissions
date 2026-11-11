class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for num in nums:
            count = count + 1 if num == 1 else 0
            res = max(count, res)
        return res