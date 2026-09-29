class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length # creates the result array 1 doesnt matter as 1*x=x

        # we will get the multiplication of the left and then multiply it by the right

        left = 1
        for i in range(length):
            result[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(length-1, -1, -1):
            result[i] *= right
            right *= nums[i]
        
        return result
        