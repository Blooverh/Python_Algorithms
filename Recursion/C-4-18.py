def whichHasMore(str):
    vowels=['a','e','i','o','u']

    if len(str) == 0:
        return 0
    if str[0] not in vowels:
        return 1 + whichHasMore(str[1:])
    else:
        return whichHasMore(str[1:])

print(whichHasMore("hoi"))
