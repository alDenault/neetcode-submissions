class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        left.append(1)
        right = []
        right.append(1)
        output = []
        for i in range (0, len(nums)-1):
            num = nums[i]
            left.append(left[-1]*num)
            num=nums[len(nums)-1-i]
            right.append(right[-1]*num)
        for i in range(0, len(nums)):
            leftproduct = left[i]
            rightproduct = right[len(nums)-1-i]
            output.append(leftproduct*rightproduct)
        return output