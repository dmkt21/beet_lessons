# task01
# Write a PY program to detect the no of local variables declared in a funct

def func():
    a = 2 + 2
    b = 2 ** 2
    return a + b


def func_number_of_integers():
    print(func.__code__.co_nlocals)


# task 02
# Write a PY  program to access a func inside a func
# (use func, which returns other func)

def pyramid_volume(a):
    def volume(h):
        return (1/3) * (a**2) * h
    return volume


def pyramid_volume_a4_fucn():
    pyramid_volume_a4 = pyramid_volume(4)
    print(pyramid_volume_a4(2))


# task03

def choose_func(nums: list, func1, func2):
    if all(True if n > 0 else False for n in nums):
        return square_nums(nums)
    else:
        return remove_negatives(nums)

nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


# additional task: зробіть рекурсивну функцію,
# що порахує суму цілих чисел в заданому діапазоні в якості аргументів


def sum_recursive(first_number, last_number):
    sum_of_numbers = 0
    if first_number > last_number:
        return sum_of_numbers
    return first_number + sum_recursive(first_number + 1, last_number)


def main():

    func_number_of_integers()
    pyramid_volume_a4_fucn()
    print(sum_recursive(1, 9))
    print(choose_func(nums1, square_nums, remove_negatives))
    print(choose_func(nums2, square_nums, remove_negatives))


if __name__ == '__main__':
    main()










