class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        # Replace subtractive pairs first so each unit stands alone
        s = (
            s.replace("IV", "a")
            .replace("IX", "b")
            .replace("XL", "c")
            .replace("XC", "d")
            .replace("CD", "e")
            .replace("CM", "f")
        )

        char_map = {
            "a": 4,
            "b": 9,
            "c": 40,
            "d": 90,
            "e": 400,
            "f": 900,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        return sum(char_map[ch] for ch in s)