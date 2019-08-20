readFile = open("data.txt", "r")
writeFile = open("insert.out", "w")
for line in readFile:
  splitLine = line.split()
  del splitLine[0]
  numArray = []
  for num in splitLine:
    numArray.append(int(num))
  for i in range(1, len(numArray)):
    replaced = False
    for j in range(0, len(numArray)):
      if numArray[i] <= numArray[j] and i > j and replaced == False:
        numArray.insert(j, numArray[i])
        del numArray[i+1]
        replaced = True
  for number in numArray:
    writeFile.write(str(number))
    writeFile.write(" ")
  writeFile.write("\n")
