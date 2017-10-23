#simple program to convert a temerature to  in celcius to fahrenheit

c = int(input("enter a temperature in celcius: "))
def cel_to_fahr(c):
  f = c * 9/5 + 32
  return f
print(str(c) + " celcius is " + str(cel_to_fahr(c)) + "fahrenheit")

