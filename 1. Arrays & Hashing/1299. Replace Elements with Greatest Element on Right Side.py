#Problem Statment: Given an array arr, replace every element in that array with the greatest element among the
#elements to its right, and replace the last element with -1.

#After doing so, return the array.

def replaceElements(arr):
    r_max = -1
    for i in range(len(arr)-1, -1, -1):
        newMax = max(r_max, arr[i])
        arr[i] = r_max
        r_max = newMax        
    return arr

arr = [17, 18, 5, 4, 6, 1]
print(replaceElements(arr))