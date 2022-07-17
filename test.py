def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


def choose_func(list_of_numbers, func1, func2):
    for i in list_of_numbers:
        return func1(i)


list_of_numbers = (1, 2, 3, 4, 5)


print(choose_func(list_of_numbers, square_nums, remove_negatives))
