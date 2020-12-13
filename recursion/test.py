class solution(object):

    def lettercasepermutewithmutable784(self, inpstr):
        res = []

        def helper(inpstr, level):
            print(inpstr)
            print(res)
            if level == len(inpstr):
                res.append("".join(inpstr))
            else:
                if inpstr[level].isdigit():
                    helper(inpstr, level+1)
                else:
                    inpstr[level] = inpstr[level].lower()
                    helper(inpstr, level+1)
                    inpstr[level] = inpstr[level].upper()
                    helper(inpstr, level+1)

        helper(list(inpstr), 0)
        return res


sol = solution()
print(sol.lettercasepermutewithmutable784("abc"))