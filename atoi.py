def atoi(s):
    s = s.strip()
    number = 0
    neg = False

    for i, char in enumerate(s):
        if char == '-' and i == 0:
            neg = True
        elif char == '+' and i == 0:
            continue
        elif char.isdigit():
            number = number*10 + int(char)
        else:
            break

    if neg:
        number = -number
    if number < -2**31:
        number = -2**31
    if number > 2**31 - 1:
        number = 2**31 - 1
    return number


s = "4193 with words"
r = atoi(s)
print()
