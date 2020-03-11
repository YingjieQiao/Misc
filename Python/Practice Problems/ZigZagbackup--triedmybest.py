class Solution:
    def convert(self, s: str, numRows: int) -> str:
        mid = numRows//2
        unit = numRows + mid
        biglist = []
        ls = []
        for char in s:
            ls.append(char)
            
        if len(ls) == 0:
            return ''
        elif len(ls) <= numRows:
            return s
        else:
            while len(ls) >= unit:
                preans = []
                i = 0
                while i < unit:
                    preans.append(ls[i])
                    i += 1
                
                i = 0
                while i < unit:
                    ls.remove(ls[0])
                    i += 1
                    
                biglist.append(preans)
                            
            i = 0
            preans = []
            while i <= len(ls)-1:
                preans.append(ls[i])
                i += 1
            biglist.append(preans)
            print(biglist)
            
            ans = []
            count = 0
            if len(biglist[-1]) == len(biglist[0]):
                while count < numRows:
                    for l in biglist:
                        if 1 <= count <= numRows-2 and len(l) != len(biglist[-1]):
                            ans.append(l[count])
                            ans.append(l[len(l)-count])
                        else:
                            ans.append(l[count])
                    count += 1
            else:
                while count < numRows:
                    if count <= len(biglist[-1])-1:
                        for l in biglist:
                            if 1 <= count <= numRows-2 and len(l) != len(biglist[-1]):
                                if len(l) != mid:
                                    ans.append(l[count])
                                    ans.append(l[len(l)-count])
                                else:
                                    ans.append(l[count])
                            else:
                                ans.append(l[count])
                        count += 1
                    else:
                        del biglist[-1]
                        for l in biglist:
                            if 1 <= count <= numRows-2:
                                if len(l) != mid:
                                    ans.append(l[count])
                                    ans.append(l[len(l)-count])
                                else:
                                    ans.append(l[count])
                            else:
                                ans.append(l[count])
                        count += 1
                        
                        
            ANS = ''.join(ans)
            return ANS