palilist = [['n', 'i', 't', 'i', 'n'], ['n', 'iti', 'n'], ['nitin']]

def printpartitions(str):
    for i in range(len(palilist)):
        for j in range(len(palilist[i])):
            print(palilist[i][j], sep="|", end="|")
        print()

printpartitions(str)
