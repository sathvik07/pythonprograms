def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    out = [''] * numRows
    line = 0
    adder = 1
    for char in s:
        out[line] += char
        if line == 0:
            adder = 1
        elif line == numRows - 1:
            adder = -1
        line += adder    
    return ''.join(out)



ans = convert("PAYPALISHIRING",10)
print(ans)