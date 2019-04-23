class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend > 0) is (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)

        def div(x: int, y: int) -> (int, int):
            if x == 0: return (0, 0)
            else:
                (q, r) = div(x>>1, y)
                q <<= 1
                r <<= 1

                if x % 2:
                    r += 1
                if r >= y:
                    r = r - y
                    q += 1
                return (q, r)

        ans, _ = div(dividend, divisor)
        ans = -ans if not positive else ans
        return min(ans, 2**31-1) if ans >= 0 else max(ans, -2**31)

    def divideFast(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)



solution = Solution()
print(solution.divide(7, -3))