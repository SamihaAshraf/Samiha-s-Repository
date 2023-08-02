#Samiha Ashraf
#1884227

def selection_sort_descend_trace(nums):
    n = len(nums)
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if nums[j] > nums[max_idx]:
                max_idx = j

        nums[i], nums[max_idx] = nums[max_idx], nums[i]

        for num in nums:
            print(num, end=' ')
        print()


if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    selection_sort_descend_trace(input_list)
