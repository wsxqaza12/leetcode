class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()
        n = len(arr)
        print(arr, n)

        if n % 2 == 0:
            return (arr[n//2-1] + arr[n//2])/2
        else:
            return arr[n//2]

# two pointer


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        from math import floor
        n = (len(nums1)+len(nums2)) // 2 + 1
        n1 = 0
        n2 = 0
        i = 0
        ans = []
        curr = 0
        print(nums1, nums2, n)

        for i in range(n):
            print(i, n1, n2)
            if n1 < len(nums1) and n2 < len(nums2):
                if nums1[n1] < nums2[n2]:
                    curr = nums1[n1]
                    n1 += 1
                else:
                    curr = nums2[n2]
                    n2 += 1
            elif n1 >= len(nums1) and n2 < len(nums2):
                curr = nums2[n2]
                n2 += 1
            elif n2 >= len(nums2) and n1 < len(nums1):
                curr = nums1[n1]
                n1 += 1

            if n == 1:
                return curr
            elif i == n-2:
                ans.append(curr)
            elif i == n-1:
                ans.append(curr)
            print('ans', ans)

        if (len(nums1)+len(nums2)) % 2 == 0:
            return sum(ans)/2
        else:
            return ans[-1]
