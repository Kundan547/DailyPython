def find_missing_element(array):
    expected_sum = sum(range(1,101))
    actual_sum = sum(array)
    return expected_sum - actual_sum

array = [x for x in range(1,101) if x not in[3,4,6,7,9]]

missing_number = find_missing_element(array)

print("The missing number is: ", missing_number)