class Activity:
    def __init__(self, activity, start, end):
        self.activity = activity
        self.start = start
        self.end = end

readFile = open("act.txt", "r")
lines = 0
iterator = 1
activitySet = []
cases = []
for line in readFile:
    if " " not in line:
        lines = int(line)
    else:
        activity, start, end = line.split(' ')
        object = Activity(int(activity), int(start), int(end))
        activitySet.append(object)
        if (iterator == lines):
            cases.append(activitySet)
            activitySet = []
            lines = 0
            iterator = 1
        else:
            iterator += 1

setNum = 1
for case in cases:
    case.sort(key=lambda c: c.end, reverse=False)
    case.sort(key=lambda c: c.start, reverse=True)
    solution = []
    first = True
    lastStart = None
    for activity in case:
        if first:
            solution.append(activity)
            first = False
            lastStart = activity.start
        else:
            if activity.end <= lastStart:
                solution.append(activity)
                lastStart = activity.start
    print ("Set " + str(setNum))
    print ("Number of activities selected = " + str(len(solution)))
    solutionString = ""
    for activity in solution:
        solutionString += str(activity.activity) + " "
    print ("Activities: " + solutionString + "\n")
    setNum += 1
