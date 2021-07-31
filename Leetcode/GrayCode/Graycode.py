class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        res = self.grayCode(n-1)
        num = 2**(n-1)
        res += res[::-1]
        for i in range(num,len(res)):
            res[i] ^= num
        return res