# Вам дано большое целое число, представленное в виде массива целых чисел digits, каждое из которых digits[i] является
# цифрой целого числа. Цифры упорядочены от наиболее значимого к наименее значимому, слева направо. Большое целое число
# не содержит ведущих нулей.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits_1 = int(''.join(map(str, digits)))
        return map(int, str(digits_1 + 1))