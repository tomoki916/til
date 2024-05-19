# class Solution(object):
#     def myPow(self, x, n):
#         """
#         :type x: float
#         :type n: int
#         :rtype: float
#         """
#         is_negative = n < 0
#         n = abs(n)

#         result = 1.0

#         def pow(x, n):
#             if n == 0:
#                 return 1

#             res = pow(x, n//2)
#             res *= res
#             if n % 2 == 1:
#                 res *= x

#             return res

#         result = pow(x, n)

#         return result if not is_negative else 1 / result

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        is_negative = n < 0
        n = abs(n)

        result = 1.0

        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n = n // 2

        return result if not is_negative else 1 / result
