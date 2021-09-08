s = "barfoothefoobarman"
words = ["foo","bar"]

while any(x in s for x in words):
     for y in words :
         if y in s :
             print(words)