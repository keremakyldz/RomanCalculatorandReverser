class Converter:
    def __init__(self):
        self.roman_letters = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        self.notValid = ["IIII", "XXXX" , "VV", "LL", "CC", "DD", "MM"]
    def romantoInt(self,roman_string):
        total_value = 0
        previous_value = 0

        if roman_string in self.notValid:
            return f"Please put valid Roman value.{roman_string} is not a valid Roman Value "
        else:
            pass

        for letter in reversed(roman_string):
            current_value = self.roman_letters.get(letter,0)

            if current_value < previous_value:
                total_value -= current_value
            else:
                total_value += current_value

            previous_value = current_value

        return total_value

class Reverser:
    def __init__(self):
        self.hmap = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
    def inttoRoman(self,num):
        result = ""

        for value in sorted(self.hmap.keys(), reverse = True):
            while num >= value:
                result += self.hmap[value]
                num -= value

        return result

roman = Converter()
print(roman.romantoInt("IV"))
print(roman.romantoInt("IIII"))

int = Reverser()
print(int.inttoRoman(1922))
print(int.inttoRoman((9)))

