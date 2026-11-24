with open("data.txt") as f:
    chars = f.read()

charCount = {
    "uppercase":{},
    "lowercase":{},
    "numbers":{},
    "special":{}
}

for char in chars:
    if char.isupper():
       category = "uppercase"
    elif char.islower():
        category = "lowercase"
    elif char.isdigit():
        category = "numbers"
    else:
        category = "special"

    if char in charCount[category]:
        charCount[category][char] += 1
    else:
        charCount[category][char] = 1

for category, chars in charCount.items():
    print(category, ":",chars)
