#Problem statement:Given an array arr, replace every element in that array with the greatest element among the
#elements to its right, and replace the last element with -1.

#After doing so, return the array.

class Solution:
    def replaceElements(self, arr):
    #creating rightmax and currmax. rightmax will hold the maximum element from right of the element, while currmax
    #will hold the current maximum. Both are initialized to -1
        rightmax, currmax = -1, -1

    #Traversing from right and updating arr[i] as per requirements.
        for i in range(-1, -len(arr)-1, -1):
            if arr[i] > currmax:
                currmax = arr[i]
            arr[i] = rightmax
            rightmax = currmax
    
        return arr

arr = [17,18,5,4,6,1]
print(Solution().replaceElements(arr))