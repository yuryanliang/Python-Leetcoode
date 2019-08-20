class TwoSum:
    def two_sum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return -1


if __name__ == "__main__":
    a_temp = input().split(",")
    a = [int(i) for i in a_temp]
    b = int(input())

    print(a_temp)
    print(b)
    print(a)

    print(TwoSum().two_sum(a, b))
