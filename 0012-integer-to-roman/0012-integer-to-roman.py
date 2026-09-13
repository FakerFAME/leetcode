class Solution:
    def intToRoman(self, num: int) -> str:
        num_map = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C",  90: "XC",  50: "L",  40: "XL",
            10: "X",   9: "IX",   5: "V",   4: "IV",
            1: "I"
        }

        res = []
        for n, sym in num_map.items():
            if num == 0:
                break
            count, num = divmod(num, n)
            if count:
                res.append(sym * count)

        return "".join(res)