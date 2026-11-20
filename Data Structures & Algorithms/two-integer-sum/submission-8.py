class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}
        index = 0
        for i in nums:
            if difference.get(target-i, -1) == -1:
                difference[i]=index
            else:
                return [difference.get(target-i), index]
            index=index+1