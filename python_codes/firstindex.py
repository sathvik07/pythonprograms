string = "aaaaa"
needle = "bba"
n = len(string)
if n == 0:
 print("")
while (needle in string):
    print(string.index(needle))
else:
    print(-1)
# if needle in string :
#  print(string.index(needle))



#n = haystack.find(needle)