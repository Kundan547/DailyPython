def find_max_element(arr):
    max_element = arr[0]
    for num in arr:
        if arr > max_element:
            max_element = num
    return max_element