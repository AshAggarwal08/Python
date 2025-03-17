user_input = input("Enter a string : ")
def splitfunc(txt):
    txt = user_input.split(" ")
    #print(txt)
    return(txt)


def joinfunc(words):
    result = "-".join(words)
    print(result)


words = splitfunc(user_input)
print(words)
joinfunc(words)
