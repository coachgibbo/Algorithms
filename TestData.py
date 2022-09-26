import random


def generate_list_of_ints(minimum, maximum, size):
    return [random.randint(minimum, maximum) for _ in range(size)]


def generate_sorted_list_of_ints_with_target(minimum, maximum, size, target):
    new_list = generate_list_of_ints(minimum, maximum, size)
    new_list[random.randint(0, size)] = target
    return sorted(new_list)
