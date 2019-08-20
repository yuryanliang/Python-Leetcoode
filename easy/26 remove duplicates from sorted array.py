"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""
class Sol:
    def rem_dup(self, nums) :
        if len(nums) == 0 :
            return 0
        s = 0 # slow
        f = 1 # fast
        while f < len(nums):
            if nums[s] != nums[f]:
                s += 1
                nums[s] = nums[f]
            f += 1
        return s + 1


def main():
    nums = [[1,2,2], [], [0,0,1,1,1,2,2,3,3,4]]
    for n in nums:
        length = Sol().rem_dup(n)
        print (n[:length])


 # Get three test score
round1 = int(raw_input("Enter score for round 1: "))
round2 = int(raw_input("Enter score for round 2: "))
round3 = int(raw_input("Enter score for round 3: "))
# Calculate the average
average = (round1 + round2 + round3) / 3
# Print out the test score %
print ("the average score is: ", average)



left = 0, right = n -1
while (left <= right)
    mid = (left + right) / 2
    case
    x[mid] < t: left = mid + 1;
    %Lx[mid] - right ; mid —-1;
    ;<[mid] = t: p = mid;
break;


if __name__ == '__main__':
    main()
