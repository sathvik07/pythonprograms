class Solution :
  def isValid(self, string: str) -> bool:
     brackets = ["()" , "{}" , "[]"]
     while any(x in string for x in brackets):
       for bracket in brackets:
           string = string.replace(bracket, "")
        #    print(string)
     return not string
# print(an)
  
ne = Solution()
string = "(){}{](}"
# ne.isValid(string)

print(string,"-","paranthesis are balanced"
        if ne.isValid(string) else "paranthesis are unbalanced")