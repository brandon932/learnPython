
import datetime

fileList = ["file1.txt","file2.txt","file3.txt"]
now  = datetime.datetime.now()
myFileName = now.strftime("%Y-%m-%d-%H-%M-%S-%f.txt")
combinedFiles = open(myFileName, 'a+')
for file in fileList:
  x = open(file,'r')
  content = x.read()
  combinedFiles.write(content + "\b")
  x.close()

combinedContents = combinedFiles.read()
combinedFiles.close()
print(combinedContents)






