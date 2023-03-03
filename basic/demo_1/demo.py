def mult_or_sum(num1: int, num2: int) -> int:
    return num1 * num2 if num1 * num2 <= 1000 else num1 + num2




result = mult_or_sum(20, 30)
print('The result is', result)

result = mult_or_sum(40, 30)
print('The result is', result)