
import random

def normal(full_capacity, heuristic=1/3):
    """
    Using normal distribution to generate a capacity between 1 and an heuristic of 1/3 of the full_capacity
    """
    real_capacity = full_capacity * heuristic
    capacity = random.normalvariate(real_capacity, full_capacity - real_capacity)
    if capacity < 0:
        capacity = 0
    return capacity

def normal_generator(full_capacity, heuristic):
    def wrapped():
        return normal(full_capacity, heuristic)
    return wrapped