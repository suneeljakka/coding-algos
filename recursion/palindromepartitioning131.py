def palindromepartitioning131(s):
    def ispalindrome(str, si, ei):
        while si < ei:
            if str[si] == str[ei]:
                si += 1
                ei -= 1
            else:
                return False
        return True

    palilist = []
    curr_palin_list = []

    def printpartitions():
        for i in range(len(palilist)):
            for j in range(len(palilist[i])):
                print(palilist[i][j], end="|")
            print()

    def helper(str, si, ei):
        if si == ei:
            palilist.append(curr_palin_list.copy())
        else:
            for i in range(si, ei):
                if ispalindrome(str, si, i):
                    curr_palin_list.append(str[si:i + 1])
                    helper(str, i + 1, ei)
                    curr_palin_list.pop()

    helper(s, 0, len(s))
    printpartitions()

# abracadabra
if __name__ == "__main__":
    palindromepartitioning131("aa")
