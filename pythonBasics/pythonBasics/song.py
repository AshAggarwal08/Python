def CamelCase(s):

  sentence = s.split

  s = sentence[0].lower() + ''.join(s.capitalize() for s in sentence[1:])

  return s
  #s=  sentence[0].lower + ''.join(s.capitalize() for s in sentence[1:])
  #return(s)
CamelCase("cats AND*Dogs-are Awesome")
print(CamelCase("cats AND*Dogs-are Awesome"))
#CamelCase("cats AND*Dogs-are Awesome")
#print(result)