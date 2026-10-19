class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # MergeSort then find out if the len of the mergedArr is even or odd
        # if the newArr is odd then get len(arr)+1/2
        # if the newArr is even then get len(arr)/2 and len(arr)/2 + 1


        sortedArr = []
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sortedArr.append(nums1[i])
                i+=1
            else:
                sortedArr.append(nums2[j])
                j+=1

        while i < len(nums1):
            sortedArr.append(nums1[i])
            i+=1

        while j < len(nums2):
            sortedArr.append(nums2[j])
            j+=1

        print(sortedArr)

        #even
        if len(sortedArr) % 2 == 0: 
            return (sortedArr[len(sortedArr)//2] + sortedArr[len(sortedArr)//2 - 1]) / 2
        else:
            return sortedArr[(len(sortedArr)) // 2] 
