def twoSum(table, target):
    for i in range(len(table)):
        for j in range(1, len(table)):
            if table[i] + table[j] == target:
                return [i, j]

print(twoSum([2, 7, 11, 15], 9))
