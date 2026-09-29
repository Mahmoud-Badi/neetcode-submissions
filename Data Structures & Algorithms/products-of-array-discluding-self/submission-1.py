class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length # 1 is safe to start with since 1*x=x

        # pass 1: left to right, record product of everything BEFORE recording, THEN fold nums[i] in
        left = 1
        for i in range(length):
            result[i] = left # everything to the left of i, not including i
            left *= nums[i]

        # pass 2: right to left, same idea but combine with what's already in result (*=, not =)
        right = 1
        for i in range(length - 1, -1, -1): # backward version of range(0, length) (start, stop, step)
            result[i] *= right # multiply in everything to the right of i, not including i
            right *= nums[i]

        return result

        # Time = O(n), Space = O(1) extra (not counting result)