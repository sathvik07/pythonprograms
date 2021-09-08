
string = "{()}{["
brackets = ["()" , "{}" , "[]"]

def isValid () :
 while any(x in string for x in brackets):
       for bracket in brackets:
           string = string.replace(bracket, "")
           print(string)
print("heyy",not string)
# print(an)


print(string,"-","balanced"
        if not string else "unbalanced")