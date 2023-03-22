def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    number=0
    while a<len(s):
        if s[a].isupper()==True:
            number = number + 1
        a = a + 1
    return number
print(main("biDM44F4"))