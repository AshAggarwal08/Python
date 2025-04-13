str = "RahulShettyAcademy.com"
str1 = "consulting firm"
str3 = "RahulShetty"

print(str[1])   #a

print(str[0:5])  # if you want substring in python

print(str+str1)   # concatenation

print(str3 in str)  # substring check

var = str.split(".")
print(var)
print(var[0])
str4 = " great "
print(str4.strip())
print(str4.lstrip())

print(str4.rstrip())

#String slicing
name = 'Tommy'
print(len(name))
print(name[-4:3])  #-4 means len-4

print(name[-1:-3])  # it would not print anything as 5-1 = 4 == y and string ends here

print(name[-3:-1]) # first argument is inclusive but second argument is exclusive.
print(name[2:3]) #m

#endwith
s = '!!!!Hey Welcome Home !!......@@@@'
print(s.endswith('@')) #true or false
print(s.endswith('@',4,10)) # is the string ending with @ in between given indices
#startwith

print('---------startswith----------')
print(s.startswith('H'))
#Center and count
print(s.center(20))
print(s.count('!'))

#replace
s4 = "Hello Maria !!!"
print(s4.replace('Mari','Yari'))

#find
s6 = 'Hey Welcome to Strings Demo , Maria!'
print(s6.find('m',0,20))


#swapcase
print(s6.swapcase())

#title
print(str1.title())




