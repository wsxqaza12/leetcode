class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        slow = 0
        ans = 0


        while slow < len(nums):
            if nums[slow] < k:
                ans += 1
            fast = slow + 1
            temp = nums[slow]
            while fast < len(nums):
                temp *= nums[fast]
                if temp < k:
                    ans += 1
                    fast += 1
                else:
                    break
            slow += 1

        return ans
    
# Time Limit Exceeded

# sliding windows
class Solution:
def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    if k <= 1:
        return 0
    
    left, right, product = 0, 0, 1
    ans = 0
    while right < len(nums):
        product *= nums[right]
        while product >= k:
            product = product / nums[left]
            left += 1
        ans += (right - left + 1)
        right += 1
    
    return ans
