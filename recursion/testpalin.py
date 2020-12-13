class solution(object):
    def testpalin(self, str):
        curr_list = []
        palin_list = []
        n = len(str)

        def ispalindrome(str, si, ei):
            while si < ei:
                if str[si] == str[ei]:
                    si += 1
                    ei -= 1
                else:
                    return False
            return True

        def helper(str, si, n):
            print(si)
            print(curr_list)
            if si == n:
                palin_list.append(curr_list.copy())

            for i in range(si, n):
                if ispalindrome(str, si, i):
                    curr_list.append(str[si:i+1])
                    helper(str, i+1, n)
                    curr_list.pop()

        helper(str, 0, len(str))
        return palin_list

sol = solution()
ret = sol.testpalin("nitin")
print(ret)



