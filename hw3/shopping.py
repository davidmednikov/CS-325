def knapsack(maxWeight, weightsArray, valuesArray, items, matrix):
    for item in range(items + 1):
        for weight in range(maxWeight + 1):
            optimal = {
                "price" : 0,
                "items" : ""
            }
            if item == 0 or weight == 0:
                matrix[item][weight] = optimal
            elif weightsArray[item - 1] <= weight:
                if valuesArray[item - 1] + matrix[item - 1][weight - weightsArray[item - 1]]["price"] > matrix[item - 1][weight]["price"]:
                    matrix[item][weight] = {
                        "price" : valuesArray[item - 1] + matrix[item - 1][weight - weightsArray[item - 1]]["price"],
                        "items" : matrix[item - 1][weight - weightsArray[item - 1]]["items"] + " " + str(item)
                    }
                else:
                    matrix[item][weight] = {
                        "price" : matrix[item - 1][weight]["price"],
                        "items" : matrix[item - 1][weight]["items"]
                    }
            else:
                matrix[item][weight] = matrix[item - 1][weight]

readFile = open("shopping.txt", "r")
writeFile = open("shopping.out", "w")
times = int(readFile.next())
lengths = []
tally = 0
gotN = False
gotNLines = False
gotF = False
gotFLines = False
n = -1
f = -1
for line in readFile:
    if(gotN is False):
        tally += 1
        gotN = True
        n = int(line)
    else:
        if(gotNLines is False):
            for i in range(n):
                tally += 1
                if(i < n - 1):
                    readFile.next()
            gotNLines = True
        else:
            if(gotF is False):
                f = int(line)
                tally += 1
                gotF = True
            else:
                if(gotFLines is False):
                    for j in range(f):
                        tally += 1
                        if(j < f - 1):
                            readFile.next()
                    gotFLines = True
                if(gotFLines is True):
                    lengths.append(tally)
                    tally = 0
                    gotN = False
                    gotNLines = False
                    gotF = False
                    gotFLines = False
                    n = -1
                    f = -1

readFile.close()
readFile = open("shopping.txt", "r")
readFile.next()
for time in range(times):
    gotItems = False
    gotInventory = False
    gotFamily = False
    gotMembers = False
    inventory = []
    items = -1
    family = -1
    members = []
    tally = 0
    for i in range(lengths[time]):
        if (tally == i):
            line = readFile.next()
            tally += 1
            if(gotItems is False):
                items = int(line)
                gotItems = True
            else:
                if(gotInventory is False):
                    for j in range(items):
                        itemLine = line
                        price, space, weight = itemLine.partition(' ')
                        newItem = {
                            "price" : int(price),
                            "weight" : int(weight)
                        }
                        inventory.append(newItem)
                        if(j < items - 1):
                            line = readFile.next()
                            tally += 1
                    gotInventory = True
                else:
                    if(gotFamily is False):
                        family = int(line)
                        gotFamily = True
                    else:
                        if(gotMembers is False):
                            for k in range(family):
                                members.append(int(line))
                                if(k < family - 1):
                                    line = readFile.next()
                                    tally += 1
                            gotMembers = True
    maxWeight = max(members)
    matrix = [[0 for x in range(maxWeight + 1)] for y in range(items + 1)]
    weightsArray = []
    valuesArray = []
    for i in range(len(inventory)):
        weightsArray.append(inventory[i]["weight"])
        valuesArray.append(inventory[i]["price"])
    knapsack(maxWeight, weightsArray, valuesArray, items, matrix)
    totalPrice = 0
    for member in members:
        totalPrice += matrix[items][member]["price"]
    writeFile.write("Test Case " + `time + 1` + "\n")
    writeFile.write("Total Price " + str(totalPrice) + "\n")
    writeFile.write("Member Items:\n")
    for i in range(family):
        writeFile.write(`i+1` + ":" + matrix[items][members[i]]["items"] + "\n")
    writeFile.write("\n")
