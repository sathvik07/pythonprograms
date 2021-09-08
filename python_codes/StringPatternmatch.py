import re

stat = input("enter the string: ")

patt = input("enter the pattern: ")

# if (re.search(stat , patt , re.IGNORECASE)==0):
if len(re.findall(patt,stat))==0:
   print("False")
if re.findall(patt,stat)[0]==stat:
    print("True")
else:
    print("False")




