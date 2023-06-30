import random
from montecarlo import capacity

def work_work(todo, capacity):
    """
    Apply the todo minus the capacity and return both results
    """
    if capacity < 0 :
        capacity = 0
    todo -= capacity
    if todo < 0:
        todo = 0
    return todo


def simulate_project_wip(todo, capacity_generator):
    """
    Iterates until the todo list is not empty
    The capacity to work is recalculated for each iteration.

    Keyword arguments:
    stream_num -- the number of streams to migrate at the beginning
    todo -- the total workload of the project. It can be equal to stream_num but it is interesting to add something not linear (e.i. gamma distribution)
    """
    current_iteration = 1
    todo_progress = [0, todo]
    iterations = [0, 1]

    while todo > 0 :
        todo = work_work(todo, capacity=capacity_generator())
        current_iteration += 1
        iterations.append(current_iteration)
        todo_progress.append(todo)
    
    return iterations, todo_progress