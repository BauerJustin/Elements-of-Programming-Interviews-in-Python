#code
def is_valid(s):
    return len(s) == 1 or (s[0] != '0' and int(s) <= 255)

def get_valid_ip_address(s):
    result = []
    parts = [None] * 4

    for i in range (1,min(4,len(s))):
        parts[0] = s[:i]
        if is_valid(parts[0]):
            for j in range(1, min(4,len(s)-i)):
                parts[1] = s[i:i+j]
                if is_valid(parts[1]):
                    for k in range(1, min(4,len(s)-i-j)):
                        parts[2] = s[i+j:i+j+k]
                        parts[3] = s[i+k+j:]
                        if is_valid(parts[2]) and is_valid(parts[3]):
                            result.append('.'.join(parts))
    return result

#tests 
print(get_valid_ip_address("19216811"))