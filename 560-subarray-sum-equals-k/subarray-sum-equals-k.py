class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict1 = {0: 1}
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num

            val = curr_sum - k

            if val in dict1:
                count += dict1[val]

            dict1[curr_sum] = dict1.get(curr_sum, 0) + 1

        return count