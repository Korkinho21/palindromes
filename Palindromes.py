def palindrome(s: str):

    if len(s) == 2:
        if s[0] == s[1]:
            return print(True)
        else:
            return print(False)

    if len(s) == 3:
        if s[0] == s[2]:
            return print(True)
        else:
            return print(False)
    
    if len(s) > 3:
        pal = False
        for i in range(len(s)):
            if s[i] == s[-i-1]:
                pal = True
            else:
                pal = False
                return print(pal)

        return print(pal)


def palindrome2(s: str):
    l = s[::-1]
    return print(l == s)


if __name__ == '__main__':
    s = 'otto'
    palindrome(s)
    palindrome2(s)