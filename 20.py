class Solution(object):
    def leftRightDifference(self, nums):
        
        result = []
        leftt = 0
        rightt = 0

        for i in range(len(nums)):
            # leftt = 0
            # rightt = 0
            leftt = sum(nums[:i])
            rightt = sum(nums[i+1:])
            print(leftt)
            print(rightt)
            result.append(abs(leftt - rightt))
        print(result)



n=[10,4,8,3]

Solution().leftRightDifference(n)

# [15,1,11,22]