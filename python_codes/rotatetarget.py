


def search (arr, key):
    h = len(arr)-1
    l = 0 
    # if l > h:
    #     return -1
    while(l <= h):
     
        mid = (l + h) // 2
        if arr[mid] == key:
            return mid
    
        if arr[l] <= arr[mid]:
    
            if key >= arr[l] and key <= arr[mid]:
                h = mid -1
            else:
                l =mid + 1
        else:
         if key >= arr[mid] and key <= arr[h]:
            l = mid + 1
         else:
            h = mid - 1
    return -1
 
arr = [4,5,6,7,0,1,2]
key = 3
i = search(arr, key)
print(i)  