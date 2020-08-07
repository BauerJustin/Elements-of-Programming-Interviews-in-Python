#code
mapping = ['0','1','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

def mnemonics(phone_number):
    def mnemonics_helper(digit):
        if digit == len(phone_number):
            result.append(''.join(partial_result))
        else:
            for c in mapping[int(phone_number[digit])]:
                partial_result[digit] = c
                mnemonics_helper(digit + 1)
    result, partial_result = [], [0] * len(phone_number)
    mnemonics_helper(0)
    return result


print(mnemonics("2276696"))