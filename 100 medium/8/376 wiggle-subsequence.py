"""
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Example 1:

Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
Example 2:

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
Example 3:

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
Follow up:
Can you do it in O(n) time?
"""

# public:
#     int wiggleMaxLength(vector<int>& nums) {
#         if (nums.empty()) return 0;
#         vector<int> p(nums.size(), 1);
#         vector<int> q(nums.size(), 1);
#         for (int i = 1; i < nums.size(); ++i) {
#             for (int j = 0; j < i; ++j) {
#                 if (nums[i] > nums[j]) p[i] = max(p[i], q[j] + 1);
#                 else if (nums[i] < nums[j]) q[i] = max(q[i], p[j] + 1);
#             }
#         }
#         return max(p.back(), q.back());
#     }
# };
class Sol:
    def wiggle(self, nums):
        if len(nums) < 2:
            return len(nums)

        length, up = 1, None

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i] and (up is None or up is False):
                length += 1
                up = True
            elif nums[i - 1] > nums[i] and (up is None or up is True):
                length += 1
                up = False

        return length




if __name__ == '__main__':
    # nums = [1,0, 0, 2, 5]
    # nums=[1,7,4,9,2,5]
    nums = [1,17,5,10,13,15,10,5,16,8]
    # print(Sol().check(nums, 0, 4))
    print(Sol().wiggle(nums))
