def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    number=0
    while a<len(s):
        if s[a].islower()==True:
            number = number + 1
        a = a + 1
    return number
print(main("bisSSSr44F4"))