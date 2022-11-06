#read specific line from a file
f = open("sample.txt", "w")
f.write("welcome to the sample file write and test your data")
f.close()

f = open("sample.txt", "r")
content = f.readlines()
print("first line is:", content[0])


