import random
import time
numbers = 500
while numbers < 4000:
  numArray = []
  for x in range(numbers):
    numArray.append(random.randint(0, 10001))

  startTime = time.time()
  for i in range(1, len(numArray)):
    replaced = False
    for j in range(0, len(numArray)):
      if numArray[i] <= numArray[j] and i > j and replaced == False:
        numArray.insert(j, numArray[i])
        del numArray[i+1]
        replaced = True
  endTime = time.time()
  elapsedTime = endTime - startTime
  print 'Array size: {}'.format(numbers)
  print 'Runtime: {}\n'.format(elapsedTime)
  numbers += 500
