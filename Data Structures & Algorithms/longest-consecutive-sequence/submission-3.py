class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxval = 0
        for num in numset:
            counter = 0
            if num-1 not in numset:
                i = num
                while i in numset:
                    i=i+1
                    counter = counter+1
                maxval = max(maxval, counter)
        return maxval