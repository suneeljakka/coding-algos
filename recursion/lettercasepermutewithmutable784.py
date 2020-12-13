class solution(object):

    def lettercasepermutewithmutable784(self, inpstr):
        res = []

        def helper(inpstr, level, slate):
            print(slate)
            if level == len(inpstr):
                res.append("".join(slate))
                return
            else:
                if inpstr[level].isdigit():
                    slate.append(inpstr[level])
                    helper(inpstr, level+1, slate)
                    slate.pop()
                else:
                    slate.append(inpstr[level].lower())
                    helper(inpstr, level + 1, slate)
                    slate.pop()
                    slate.append(inpstr[level].upper())
                    helper(inpstr, level + 1, slate)
                    slate.pop()

        helper(inpstr, 0, [])
        return res


sol = solution()
print(sol.lettercasepermutewithmutable784("abc"))