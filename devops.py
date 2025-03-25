def multiply_by_unit_digit(numbers):
    result = [num * (abs(num) % 10) for num in numbers]
    return result
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
output = multiply_by_unit_digit(numbers)
print("Result:", output)
