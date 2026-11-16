class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        rec = {}
        for num in nums:
            rec[num] = rec.get(num,0)+1
        return list(map(lambda x: x[0], sorted(rec.items(), key=lambda item: item[1], reverse=True)))[:k]

        