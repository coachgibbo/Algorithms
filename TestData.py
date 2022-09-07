import random


def generate_list_of_ints(minimum, maximum, size):
    return [random.randint(minimum, maximum) for _ in range(size)]
