def max_subarray_sum(nums):
    if not nums:
        return []

    max_sum = current_sum = nums[0]
    start = end = temp_start = 0

    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return nums[start:end+1]

# Take input from the user
user_input = input("Enter a list of numbers separated by commas: ")
input_list = [int(x) for x in user_input.split(',')]

# Call the function
result = max_subarray_sum(input_list)

# Display the result
print("Input:", input_list)
print("Output:", result)

