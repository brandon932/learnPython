
x = input("what file would you like to read? ")
file = open(x,'r')
contents = file.readlines()
file.close()
for content in contents:
  print(content.rstrip("\n"))
