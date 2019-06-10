def romanToInt(s):
    numberal_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    decimal = 0
    for i in range(len(s)):
        if i > 0 and numberal_map[s[i]] > numberal_map[s[i - 1]]:
            decimal+=numberal_map[s[i]]-2*numberal_map[s[i-1]]
        else:
            decimal += numberal_map[s[i]]
    return decimal