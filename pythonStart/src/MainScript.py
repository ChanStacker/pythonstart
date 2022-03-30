import os
#r"C:\Users\chann\Documents\Source\Experimental\PythonStart\pythonStart\src\TestFile.txt"
dirName = os.path.dirname(__file__)
print(dirName)
fileName = os.path.join(dirName, r"TestFile.txt")

def ReadLines(f):
    print("Lines will be read")
    content = f.readlines()
    print("Lines have been read")
    print("Number of lines" + str(content.count))
    for line in content:
        print(line)

def WriteLines(f, lines):
    print("Lines will be written")
    f.writelines(lines)
    
if not os.path.isfile(fileName):
    print('File does not exist.')
else:
    print('Will be overwriting the file')
    with open(fileName, 'r+') as f:
        ReadLines(f)
        WriteLines(f, "Written by python\n")
        ReadLines(f)

