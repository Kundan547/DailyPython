def get_fibonacci_sequence(n):
    """Generate first n numbers of Fibonacci sequence"""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def replace_nines_with_fibonacci(number):
    """
    Replace each 9 in the input number with the next number 
    in the Fibonacci sequence (starting with 0,1,1,2,...)
    """
    # Convert number to string to process digits
    num_str = str(number)
    
    # Count how many 9's we need to replace
    count_nines = num_str.count('9')
    
    # Get enough Fibonacci numbers
    fib_sequence = get_fibonacci_sequence(count_nines)
    
    # Replace each 9 with the corresponding Fibonacci number
    result = ''
    fib_index = 0
    
    for digit in num_str:
        if digit == '9':
            result += str(fib_sequence[fib_index])
            fib_index += 1
        else:
            result += digit
    
    return int(result)

test_cases = [
    9999,
    1923949,
    123459,
    9876543
]

for test in test_cases:
    result = replace_nines_with_fibonacci(test)
    print(f"Original: {test} -> Result: {result}")