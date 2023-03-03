def first_eq_last(nums: list) -> bool:
    return nums[0] == nums[-1]



numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print('Given list', numbers_x, sep=': ')
print('result is', first_eq_last(numbers_x))

print('')

print('Given list', numbers_y, sep=': ')
print('result is', first_eq_last(numbers_y))