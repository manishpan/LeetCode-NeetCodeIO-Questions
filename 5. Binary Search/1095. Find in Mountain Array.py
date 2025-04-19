# Problem Statement: You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

# You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

# MountainArray.get(k) returns the element of the array at index k (0-indexed).
# MountainArray.length() returns the length of the array.
# Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

class MountainArray(object):
   def __init__(self, object):
       self.arr = object

   def get(self, index):
       return self.arr[index]

   def length(self):
       return len(self.arr)

class Solution(object):
    # We need to first find peak element that divides the Mountain arrya into ascending and descending sorted arrays. We then check the left ascending array first, since it is asked to return minimum index. If the target is not found in left part only then we search it in the right part of array.
    def findInMountainArray(self, target, mountainArr):
        n = mountainArr.length()

        def findPeak():
            start, end = 1, n - 2
            while start < end:
                mid = start + ((end - start) >> 1)

                if mountainArr.get(mid) < mountainArr.get(mid+1):
                    start = mid + 1
                else:
                    end = mid
            
            return start
        
        def binarySearch(start, end, asc = True):
            while start <= end:
                mid = start + ((end - start) >> 1)
                nums_mid = mountainArr.get(mid)

                if nums_mid == target:
                    return mid
                elif nums_mid < target:
                    if asc:
                        start = mid + 1
                    else:
                        end = mid - 1
                else:
                    if asc:
                        end = mid - 1
                    else:
                        start = mid + 1
            
            return -1
        

        peak = findPeak()

        res = binarySearch(0, peak)
        if res == -1:
            res = binarySearch(peak+1, n-1, False)
        return res

# Testcases:
mountainArr = MountainArray([1,2,3,4,5,3,1])
target = 3
print(Solution().findInMountainArray(target, mountainArr))

mountainArr = MountainArray([0,1,2,4,2,1])
target = 3
print(Solution().findInMountainArray(target, mountainArr))