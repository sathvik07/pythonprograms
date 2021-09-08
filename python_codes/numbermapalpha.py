digits = "23"

hashMap = {
    '2' : 'abc',
    '3' : 'def',
    '4' : 'ghi',
    '5' : 'jkl',
    '6' : 'mno',
    '7' : 'pqrs',
    '8' : 'tuv',
    '9' : 'wxyz'
 }


setofcombine = []

for digit in digits :
    if not setofcombine:
        setofcombine.extend(list(hashMap[digit]))
    else:
        new = []
        for combo in setofcombine :
            for letter in hashMap[digit]:
                new.append(combo + letter)
        setofcombine = new


print(setofcombine)
