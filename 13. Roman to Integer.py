#Римские цифры представлены семью различными символами  : I, V, X, L, Cи D.M
#Значение символа
#я 1
#В 5
#х 10
#л 50
#С 100
#Д 500
#М 1000

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary_num = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res=0
        n=len(s)
        for i in range(n):
            if dictionary_num[s[n-1-i]] > dictionary_num[s[n-i-2]] and i+1 < len(s):
                res -= dictionary_num[s[n-i-2]]
               
            else:
                res += dictionary_num[s[n-i-2]]
        return res