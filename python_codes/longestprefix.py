

strs  = ["flowers","flow","flight"]

# if len(lt) == 0:
#     print( "")
    
# sm = len(lt[0])
# for each in lt:
#     sm = min(sm,len(each))

# if sm == 0:
#     print("")

# pre = ""
# for i in range(sm):
#       v = lt[0][i]
#       for each in lt:
#           if each[i] != v:
#             #   print("hii")
#               print(pre)

#       pre += v

# print (pre)


# if len(strs) == 0:
#         print("")
    
# 	#find length of smallest string because the longest prefix could be the one if all the characters in the smallest string is same
	
# sm = len(strs[0])
# for each in strs:
#         sm = min(sm,len(each))
    
# 	#if the smallest string i.e in the list of strings given if any string is null then we return the empty string
# if sm == 0:
#     print("")
    
#     #we iterate and check each character of all string 
# c = ""
# for i in range(sm):
#         v = strs[0][i]
#         for each in strs:
#             if each[i] != v:
#                 print(c)
            
#         c += v
    
# print(c)


smallest = min(strs, key = len)
string = ''
for i in range(len(smallest)):
            prev = strs[0][i]
            if all(word[i] == prev for word in strs[1:]):
                string += prev
            else:
                break
print(string)