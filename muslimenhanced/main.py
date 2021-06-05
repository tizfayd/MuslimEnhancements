import os
import re



def string_not_found(string1, string2):
    if re.search(r"\b" + re.escape(string1) + r"\b", string2):
        return False
    return True
myFiles = []
count = 0
delstr = str(input("Enter your string"))
delList = []

for r, d, f in os.walk(os.getcwd()):
    for file in f:
        if '.txt' in file:
            myFiles.append(os.path.join(r, file))

print(myFiles)
for i in myFiles:
    # print(i)
    f = open(i, encoding="ISO-8859-1")
    s = f.read()
    f.close()
    if string_not_found(delstr, s):
        delList.append(i)
        count = count + 1
input(str(count) + " text file(s) will be removed. Press any key to continue ")
for i in delList:
    if os.path.exists(i):
        os.remove(i)
    else:
        print("The file does not exist: " + i)
