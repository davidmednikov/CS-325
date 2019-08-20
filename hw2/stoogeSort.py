def stoogeSort(array, leftIndex, rightIndex):
  if leftIndex >= rightIndex:
    return
  if array[leftIndex] > array[rightIndex]:
    temp = array[leftIndex]
    array[leftIndex] = array[rightIndex]
    array[rightIndex] = temp
  if rightIndex - leftIndex + 1 > 2:
    pivot = int((rightIndex - leftIndex + 1) / 3)
    stoogeSort(array, leftIndex, rightIndex - pivot)
    stoogeSort(array, leftIndex + pivot, rightIndex)
    stoogeSort(array, leftIndex, rightIndex - pivot)

readFile = open("data.txt", "r")
writeFile = open("stooge.out", "w")
for line in readFile:
  splitLine = line.split()
  del splitLine[0]
  numArray = []
  for num in splitLine:
    numArray.append(int(num))
  stoogeSort(numArray, 0, len(numArray) - 1)
  for number in numArray:
    writeFile.write(str(number))
    writeFile.write(" ")
  writeFile.write("\n")
