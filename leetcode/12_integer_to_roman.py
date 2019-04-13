def intToRoman(num: int) -> str:
        Roman: str = ''
        temp: str = ''
        for step, R in enumerate([['I', 'V', 'X'], ['X', 'L', 'C'], ['C', 'D', 'M']]):
            n = num - int(num / 10) * 10
            if n == 0:
                num = int(num/10)
                continue
            elif 1 <= n < 4: temp = n*R[0]
            elif 4 <= n <9:
                if (n-5) <= 0: temp = (5-n)*R[0]+R[1]
                else: temp = R[1] + (n-5)*R[0]
            else:
                temp = R[0] + R[2]

            Roman = temp + Roman
            num = int(num/10)

        if num > 0:
            Roman = 'M'*num + Roman

        return Roman

print(intToRoman(10))