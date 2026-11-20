class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if seen.get(num, -1) == -1:
                seen[num] = num
            else:
                return True
        return False