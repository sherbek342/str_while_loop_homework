def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    number=0
    while a<len(s):
        if s[a].isalpha()==True:
            number = number + 1
        a = a + 1
    return number
print(main("bir44F4"))
    