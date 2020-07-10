



file = open("C:\\Users\\indrasen\\Downloads\\FilePractice\\TestFile.txt", "r")
#print(file)
print(type(file))
d = dict()
#print(d)
for line in file:
    line = line.strip()
    #print(line)
    line = line.lower()
    #print(line)
    words = line.split(" ")
    print(words)
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
print(d)
for key in list(d.keys()):
    print(key, ":" , d[key])


