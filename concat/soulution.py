import glob2
import datetime

filenames=glob2.glob("*.txt")
name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f.txt")
with open(name, 'w') as file:
  for filename in filenames:
    with open(filename,"r") as f:
      file.write(f.read()+"\n")

