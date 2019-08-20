def mergeSort(array):
  if len(array) > 1:
    midpoint = len(array) // 2
    leftHalf = array[:midpoint]
    rightHalf = array[midpoint:]
    mergeSort(leftHalf)
    mergeSort(rightHalf)

    leftIterator = 0
    rightIterator = 0
    listIterator = 0

    while leftIterator < len(leftHalf) and rightIterator < len(rightHalf):
      if leftHalf[leftIterator] < rightHalf[rightIterator]:
        array[listIterator] = leftHalf[leftIterator]
        leftIterator += 1
      else:
        array[listIterator] = rightHalf[rightIterator]
        rightIterator += 1
      listIterator += 1

    while leftIterator < len(leftHalf):
      array[listIterator] = leftHalf[leftIterator]
      leftIterator += 1
      listIterator += 1

    while rightIterator < len(rightHalf):
      array[listIterator] = rightHalf[rightIterator]
      rightIterator += 1
      listIterator += 1

readFile = open("data.txt", "r")
writeFile = open("merge.out", "w")
for line in readFile:
  splitLine = line.split()
  del splitLine[0]
  numArray = []
  for num in splitLine:
    numArray.append(int(num))
  mergeSort(numArray)
  for number in numArray:
    writeFile.write(str(number))
    writeFile.write(" ")
  writeFile.write("\n")
