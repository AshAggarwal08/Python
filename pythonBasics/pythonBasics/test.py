def tuple_slice(startIndex, endIndex, tup):
    s= ",".join(tup[startIndex:endIndex])
    return (s)
    print(s)


if __name__ == "__main__":
    print(tuple_slice(3, 3, (76, 34, 13, 64, 12)))

    # should return the string "34,13,64"

    SOLVE THIS