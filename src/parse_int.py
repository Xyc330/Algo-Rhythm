keywords = {
    "and": 0,
    "zero": 0,
    "a": 1, # a hundred
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 7,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "eightteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
    "hundred": 100,
    "thousand": 1000,
    "million": 1_000_000,
}

def get_joint_value(s: str) -> int:
    arr = s.split("-")
    return keywords.get(arr[0]) + keywords.get(arr[1])

def parse_int(s: str):
    print(s)
    words = s.lower().split(" ")

    res = 0
    temp = 0
    
    for word in words:
        if word == "million":
            return 1_000_000
        if word == "thousand":
            res += temp * 1000
            temp = 0
        elif word == "hundred":
            temp *= 100
        elif "-" in word:
            temp += get_joint_value(word)
        elif keywords.get(word) is not None:
            temp += keywords.get(word)
        else:
            return "Invalid number, learn to write"
            
            
        
    res += temp
    return res



