def div_by_five(nums: list) -> tuple:
    return tuple((n for n in nums if n % 5 == 0))


num_x = [10, 20, 33, 46, 55]
mults = div_by_five(num_x)
print('Divisible by 5', *mults, sep='\n')
