class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #nums has length 2 or more
        #els in num can be any number
        #[2,4,6,3] -> [72,36,24,48]
        #[2,2] -> [2,2]

        left = [1]
        for num in nums[:-1]:
            left.append(left[-1]*num)
        right = [1]
        for num in reversed(nums[1:]):
            right.append(right[-1]*num)
        right.reverse()

        output = []
        for i in range(len(left)):
            output.append(left[i]*right[i])
        return output
 