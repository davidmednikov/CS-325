import random
import time

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

numbers = 100
while numbers < 800:
  numArray = []
  for x in range(numbers):
    numArray.append(random.randint(0, 1001))

  startTime = time.time()
  stoogeSort(numArray, 0, numbers - 1)
  endTime = time.time()

  elapsedTime = endTime - startTime
  print 'Array size: {}'.format(numbers)
  print 'Runtime: {}\n'.format(elapsedTime)
  numbers += 100
