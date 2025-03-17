#Task
#Read a given string, change the character at a given index and
#then print the modified string.

def mutate_string(string,index,char):
    l = list(string) #converted string to list because string is non mutable
    l[index] = char #replace third index by given char
    string = "".join(l)
    print(string)
    return string

mutate_string("Hello", 3, 'T')

##### second way of doing this is using slicing
def string_mutation(string, index, char):
    str1 = string[:index] + char + string[index+1:]
    print(str1)
    return

string_mutation("Ashwini", 3, 'T')
