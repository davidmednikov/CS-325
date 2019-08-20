import random
import time

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

numbers = 500
while numbers < 4000:
  numArray = []
  for x in range(numbers):
    numArray.append(random.randint(0, 10001))

  startTime = time.time()
  mergeSort(numArray)
  endTime = time.time()

  elapsedTime = endTime - startTime
  print 'Array size: {}'.format(numbers)
  print 'Runtime: {}\n'.format(elapsedTime)
  numbers += 500
