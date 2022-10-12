roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
class Solution:
    def romanToInt(self, S: str) -> int:
        summ= 0
        for i in range(len(S)-1,-1,-1):
            num = roman[S[i]]
            if 3*num < summ:
                summ = summ-num
            else:
                summ = summ+num
        return summ
if __name__ == '__main__':
    sol=Solution()
    print(sol.romanToInt("VIII"))


class Solution_2:
    def romanToInt(self, s: str) -> int:
        y=0
        for i in range(len(s)):
            if i> 0 and roman[s[i]]>roman[s[i-1]]:
                y+=roman[s[i]]-2*roman[s[i-1]]
            else:
                y+=roman[s[i]]
        return y
if __name__ == '__main__':
    sol=Solution_2()
    print(sol.romanToInt("IX"))
