s = "babad"
#ns = ''

res = ''                        
max_len = 0
        
        
for i in range(len(s)):

            l, r = i, i                 
            while l >= 0 and r < len(s) and s[l] == s[r]:   
                curr_len = r - l + 1
                if curr_len > max_len:      
                    res = s[l:r + 1]
                    max_len = curr_len
                l -= 1                      
                r += 1    
            l, r = i, i+1
print(res)

            # while l >= 0 and r < len(s) and s[l] == s[r]:
            #     curr_len = r - l + 1
            #     if curr_len > max_len:
            #         res = s[l:r + 1]
            #         max_len = curr_len
            #     l -= 1
            #     r += 1
                



