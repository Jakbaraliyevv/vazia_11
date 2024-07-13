class Solution(object):
    def containsDuplicate(self, nums):
        lst = []
        lst = set(nums)

        # 2 - variyant 
        for i in nums:
            if not i in lst:
                lst.append(i)


        if len(lst) != len(nums):
            return True
        else: 
            return False



        


nums = [1,2]
print(Solution().containsDuplicate(nums))
