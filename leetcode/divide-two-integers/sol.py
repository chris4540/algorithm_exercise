"""
https://leetcode.com/problems/divide-two-integers/description/

https://playandlearntocode.com/article/integer-division-algorithm-python-leetcode
"""

class Answer:
    MIN_INT = pow(-2, 31)
    MAX_INT = pow(2, 31) - 1

    def recursive_divide(self, current_dividend: int, current_divisor: int):
        quotient = 1
        accumulator = current_divisor  # same as current_divisor * quotient because quotient == 1 at this point
        # base case
        if current_dividend < current_divisor:
            return 0
        elif current_dividend == current_divisor:
            return 1

        while accumulator < current_dividend:
            quotient = quotient << 1
            accumulator = accumulator << 1  # implicit quotient inclusion here!

        # undo the last step, because accumulator is now larger than current_dividend
        accumulator = accumulator >> 1
        quotient = quotient >> 1
        return quotient + self.recursive_divide(current_dividend - accumulator, current_divisor)

    def divide(self, dividend: int, divisor: int) -> int:
        '''
        Main method of this module.
        :param dividend:
        :param divisor:
        :return:
        '''
        # determine the sign of quotient:
        negative = False
        if (dividend >= 0 and divisor >= 0):
            negative = False
        elif (dividend < 0 and divisor >= 0):
            negative = True
        elif (dividend > 0 and divisor <= 0):
            negative = True

        # extract positive values of dividend and divisor:
        abs_dividend, abs_divisor = abs(dividend), abs(divisor)

        # watch for limits:
        if (abs_divisor == 1):
            if (negative == True):
                return -abs_dividend if Solution.MIN_INT < -abs_dividend else Solution.MIN_INT
            else:
                return abs_dividend if Solution.MAX_INT > abs_dividend else Solution.MAX_INT

        q = self.recursive_divide(abs_dividend, abs_divisor)
        return q if negative == False else -q

class Solution2:
    def divide(self, dividend: int, divisor: int) -> int:
        INT32_MIN = -2**31
        INT32_MAX =  2**31 - 1
        d=abs(dividend)
        dv=abs(divisor)
        output=0
        while(d>=dv):
            temp=dv
            mul=1
            while(d>=temp):
                d-=temp
                output+=mul
                mul+=mul
                temp+=temp
        if(dividend<0 and divisor>=0)or(dividend>=0 and divisor<0):
            output=-output
        return min(INT32_MAX,max(INT32_MIN,output))

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        is_neg = False
        if dividend < 0 and divisor > 0:
            is_neg = True
            dividend = dividend * -1
        elif dividend > 0 and divisor < 0:
            is_neg = True
            divisor = divisor * -1
        elif dividend < 0 and divisor < 0:
            is_neg = False
            divisor = divisor * -1
            dividend = dividend * -1

        ans = dividend
        quotient = 0
        while ans >= divisor:
            ans -= divisor
            quotient += 1


        if is_neg:
            return -quotient

        return quotient



if __name__ == "__main__":
    solution = Solution()
    ans = solution.divide(1, 1)
    print(ans)


