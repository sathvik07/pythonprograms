s = ""
# n = len(s)
# su = 0
# max = 0
# ob = 0
# cb = 0

# for i in range(n):
            
#         if str[i] == '(':
#             ob += 1
#             su += 1
   
#         elif str[i] =='0' and n>=1:
#             cb += 1
#             su -= 1

#         max = su
                
#         if su == 0 :
#             max = i+1
# print(max)
# _______________________________________
# ob =0
# cb =0
# lb =0


# for i in range(n):
#         if n == 0:
#             ans = 0

#         if s[i] =='(' and n >= 0:
#             ob += 1
#         else:
#             cb += 1


#         if ob > cb:
#            lb = ob - cb
#            ans = cb + (ob - lb)
        
#         else:
#             lb = cb - ob 
#             ans = ob + (cb - lb)

#         if ob == cb :
#             ans = 0

# print(ans)



lv = [0]*(len(s)+1)
para = []
ans = 0

for i in range(len(s)):
    if s[i] == '(':
        para.append(i)
    elif s[i] == ')' and len(para) >= 1:
        sp = para.pop(len(para)-1)
        lv[i] = lv[sp-1] + (i - sp + 1)
        ans = max(ans,lv[i])

print(ans)


        

