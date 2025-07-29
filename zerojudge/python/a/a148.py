while True:
    try:
        grades = list(map(int, input().split()))
        average = 0
        for i in range(1, len(grades)):
            average += grades[i]
        average = average/grades[0]
        if average > 59:
            print("no")
        else:
            print("yes")
    except:
        break
