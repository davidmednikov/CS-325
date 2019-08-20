import random
import time
numbers = 500
while numbers < 4000:
  numArray = []
  for x in range(numbers):
    numArray.append(random.randint(0, 10001))

  for i in range(1, len(numArray)):
    replaced = False
    for j in range(0, len(numArray)):
      if numArray[i] <= numArray[j] and i > j and replaced == False:
        numArray.insert(j, numArray[i])
        del numArray[i+1]
        replaced = True

  bestStartTime = time.time()
  for i in range(1, len(numArray)):
    replaced = False
    for j in range(0, len(numArray)):
      if numArray[i] <= numArray[j] and i > j and replaced == False:
        numArray.insert(j, numArray[i])
        del numArray[i+1]
        replaced = True
  bestEndTime = time.time()
  bestEelapsedTime = bestEndTime - bestStartTime
  print 'Array size: {}'.format(numbers)
  print 'Best Case Runtime: {}\n'.format(bestEelapsedTime)

  numArray = list(reversed(numArray))
  worstStartTime = time.time()
  for i in range(1, len(numArray)):
    replaced = False
    for j in range(0, len(numArray)):
      if numArray[i] <= numArray[j] and i > j and replaced == False:
        numArray.insert(j, numArray[i])
        del numArray[i+1]
        replaced = True
  worstEndTime = time.time()
  worstElapsedTime = worstEndTime - worstStartTime
  print 'Array size: {}'.format(numbers)
  print 'Worst Case Runtime: {}\n'.format(worstElapsedTime)

  numbers += 500
