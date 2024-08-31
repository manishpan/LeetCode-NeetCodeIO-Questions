#Problem statement:Given an array arr, replace every element in that array with the greatest element among the
#elements to its right, and replace the last element with -1.

#After doing so, return the array.

class Solution:
    def replaceElements(self, arr):
    #creating currmax=-1, we will hold arr[i] to a variable and then replace it with currmax after replacing we will update currmax if tmp > currmax.
        currmax = -1

    #Traversing from right and updating arr[i] as per requirements.
        for i in range(len(arr)-1, 0, -1):
            tmp = arr[i]
            arr[i] = currmax
            currmax = max(currmax, tmp)

        return arr

arr = [17,18,5,4,6,1]
print(Solution().replaceElements(arr))