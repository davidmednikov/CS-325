import sys
fileName = sys.argv[1]

class Wrestler:
    def __init__(self, name, rivals):
        self.name = name
        self.rivals = rivals

def getRivals(name):
    returnList = []
    for rivalry in rivalries:
        wrestler, rival = rivalry.split(' ')
        if wrestler == name:
            returnList.append(rival)
        if rival == name:
            returnList.append(wrestler)
        returnList = list(set(returnList))
    return returnList

readFile = open(fileName, "r")
wrestlersList = []
wrestlers = []
rivalries = []
babyfaces = []
heels = []

totalWrestlers = int(readFile.next())
for i in range(totalWrestlers):
    wrestlersList.append(readFile.next().strip())
totalRivalries = int(readFile.next())
for j in range(totalRivalries):
    rivalries.append(readFile.next().strip())
first = True
for wrestler in wrestlersList:
    rivals = getRivals(wrestler)
    wrestlerObject = Wrestler(wrestler, rivals)
    wrestlers.append(wrestlerObject)
first = True
for wrestler in wrestlers:
    if first:
        babyfaces.append(wrestler.name)
        rivals = wrestler.rivals
        for rival in rivals:
            heels.append(rival)
        first = False
    else:
        rivals = wrestler.rivals
        for rival in rivals:
            if wrestler.name in babyfaces:
                if rival not in heels:
                    heels.append(rival)
            elif wrestler.name in heels:
                if rival not in babyfaces:
                    babyfaces.append(rival)
            else:
                babyfaces.append(wrestler.name)
                for rival in rivals:
                    if rival not in heels:
                        heels.append(rival)
possible = True
for heel in heels:
    if heel in babyfaces:
        possible = False
for babyface in babyfaces:
    if babyface in heels:
        possible = False
if possible:
    print('Yes Possible')
    babyfacesPrint = ''
    heelsPrint = ''
    for babyface in babyfaces:
        babyfacesPrint = babyfacesPrint + babyface + '  '
    print('Babyfaces:  %s' % babyfacesPrint)
    for heel in heels:
        heelsPrint = heelsPrint + heel + '  '
    print('Heels:  %s' % heelsPrint)
else:
    print ('Impossible')
