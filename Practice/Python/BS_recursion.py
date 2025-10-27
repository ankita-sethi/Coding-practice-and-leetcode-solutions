# def binary_search(arr,low,high,x):
#     if high>=low:
#         mid=(high+low)//2
#         if arr[mid]==x:
#             return mid
#         elif arr[mid]<x:
#             return binary_search(arr,mid+1,high,x)
#         else:
#             return binary_search(arr,low,mid-1,x)
#     else:
#         return -1
    
def binary_search_iter(arr, x):
    low =0
    high = len(arr)-1
    while(low<=high):
        mid = (low+high)//2
        if arr[mid]==x:
            return True
        elif arr[mid]<x:
            low = mid+1
        else:
            high = mid-1
    return False


n= int(input('enter length of array '))
arr= list(map(int, input().split(' ')))

# for i in range(n):
#     element = int(input('enter input'))
#     arr.append(element)
# print(arr)

x=int(input('enter target '))
print(binary_search_iter(arr, x))

# result=binary_search(arr,0,len(arr)-1,x)

# if result !=-1:
#     print("element found at ",str(result))
# else:
#     print("element not found")