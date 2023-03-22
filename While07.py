def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    number=0
    while a<len(s):
        if s[a].isdigit :
            if int(s[a])%2 != 0:
                number = number + 1
        a = a + 1
    return number
print(main("bisSSSr44F4"))