
def length(s):
  if type(s) == int:
    print ( "intergers do not have lengths ")
  elif type(s) == float:
    print ( "floats do not have lengths ")
  else:
    print (len(s) )

#mystr = input("input any string: " )
mystr = 2.3

length(mystr)
length("hello")
