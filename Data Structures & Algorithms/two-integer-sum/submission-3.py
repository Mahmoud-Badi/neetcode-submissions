class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = {} #hashmap to keep values in check instead of looping twic which make it n^2

        for i in range(len(nums)):
            x = target - nums[i]
            # x is the other possible number thats sums to target with i
            
            # now we check is x available in hashMap rn
            if x in hashMap:
                return [hashMap[x], i]
            
            # if not then we add i to the hashmap then try the next index
            hashMap[nums[i]] = i        