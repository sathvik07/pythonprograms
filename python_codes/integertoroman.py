ROMAN = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'V'),(1,'I')]



def numtoRoman():
    num = int(input("enter the integer"))
    roman = ''

    while num > 0:
        for i ,r in ROMAN:
            while num >= i:
                roman += r
                num -=i



    return roman


roma = numtoRoman()
print(roma)