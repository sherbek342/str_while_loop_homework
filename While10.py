def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0
    num = 0
    while a < len(s):
        if int(s[a])%2==0:
            num += int(s[a])
        a = a +1
    return num
print(main("1278"))