''''
Write a Python class to convert
a roman numeral to an integer
'''
class Roman_number_to_int:

     def romanToInt(self, s):
         roman_number = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                         'IV': 4, 'IX': 9, 'XL': 40,
                         'XC': 90, 'CD': 400, 'CM': 900}
         i = 0
         while s:
             div=s//roman_number.values(i)
             s%=roman_number(i)
             print(s)
             i+=1


if __name__ == '__main__':
    dic_roman_number = Roman_number_to_int()
    print(dic_roman_number.romanToInt("123"))

