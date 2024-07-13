class Solution(object):
    def searchInsert(self, nums, target):

        nums = sorted(nums+[target])
        print(nums)
        # for i in range(len(nums)):
        #     if target == nums[i]:
        #         return i        
        # for i in range(len(nums)):
        #     if nums[i] == target :
        #         return i  

        # for i in range(len(nums)):
        #     if nums[i] > target:
        #         return i
        # return len(nums)









nums = [1,3,5,6,7]

print((Solution().searchInsert(nums,4)))