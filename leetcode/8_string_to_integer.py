def myAtoi(s: str) -> int:
        if s == "":
            return 0
        index = []
        output = ''
        symbol_flag = False
        no_flag = False
        for step, i in enumerate(s):
            if i in ['+', '-'] and not no_flag:
                if symbol_flag:
                    return 0
                else:
                    symbol_flag = True
                    output += i
                    index.append(step)
                    continue
            elif i in ['+', '-'] and no_flag:
                break
            elif i == ' ':
                if symbol_flag:
                    break
                else:
                    continue
            elif ord(i) in range(ord('0'), ord('9')+1):
                no_flag = True
                output += i
                index.append(step)
            else:
                break

            if len(index) > 1 and index[-1] - index[-2] != 1:
                output = output[:-1]
                break
        if (symbol_flag and len(output)>1) or (not symbol_flag and len(output)):
            output = int(output)
        else: return 0
        if output > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif output < -2 ** 31:
            return -2 ** 31
        else:
            return output

print(myAtoi("-5-"))