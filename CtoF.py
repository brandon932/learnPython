#simple program to convert a temerature to  in celcius to fahrenheit

def cel_to_fahr(c):
  if c < -273.15:
    print("how is that possible")
  else:
    f = c * 9/5 + 32
    print(str(c) + " celcius is " + str(f) + " fahrenheit")
    return f

def main():
  c = float(input("enter a temperature in celcius: "))
  cel_to_fahr(c)

def test():
  temp = [10,-20,-289,100]
  for c in temp:
    cel_to_fahr(c)

def tofile():
  temp = [10,-20,-289,100]
  file = open("temp.txt",'w+')
  for t in temp:
    x = cel_to_fahr(t)
    if x != None:
      file.write(str(x) +"\n")
  file.close()

#test()
#main()
tofile()


