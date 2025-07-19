class Solution(object):
    def productExceptSelf(self, nums):
        res = 1
        zeros = 0
        products = []
        for num in nums:
            if num == 0:
                zeros += 1
                if zeros == 2:
                    return [0 for _ in range(len(nums))]
                continue
            res *= num
        if zeros != 1:
            for num in nums:
                if num == 0:
                    products.append(0)
                else:
                    products.append(res // num)
        else:
            for num in nums:
                if num == 0:
                    products.append(res)
                else:
                    products.append(0)
        return products

        """
        :type nums: List[int]
        :rtype: List[int]
        """
