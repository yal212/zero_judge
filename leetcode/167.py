class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while True:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1, right+1]
            elif s > target:
                right -= 1
            elif s < target:
                left += 1
