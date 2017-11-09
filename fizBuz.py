
for x in range(100):
  output = ""
  if x % 3 == 0:
    output += "Fiz"
  if x % 5 == 0:
    output += "Buzz"
  if output == "":
    print(x)
  else: 
    print(output)


