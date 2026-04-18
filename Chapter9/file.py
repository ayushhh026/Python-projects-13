'''f  = open("Chapter9/file.txt")
data = f.read()
print(data)
f.close()'''

'''st = "Ayush you are amazing"
f = open("Chapter9/myfile.txt","w")
f.write(st)
f.close()'''

f = open("Chapter9/file.txt")
lines = f.readlines()
print(lines,type(lines))
f.close()
f = open("Chapter9/file.txt")
lines = f.readline()
print(lines,type(lines))
f.close()