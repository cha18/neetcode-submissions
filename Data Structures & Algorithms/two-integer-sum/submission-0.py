class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict={}

        for i in range(len(nums)):
            dict[nums[i]]=i
        for i in range(len(nums)):
            diff=target-nums[i]
            diff_ix = dict.get(diff)
            if diff_ix == i: continue
            elif diff_ix != None: return sorted([diff_ix, i])
        
        '''
        learnt:
        - 'in' keyword can be use on dicts
        - choose better variable names ('dict' is bad)
        - no need to populate entire dict always. in this case, 
        the dict only needs to hold past values, so we can populate as 
        we go.
        '''


        '''
        SOLUTION

        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


        '''