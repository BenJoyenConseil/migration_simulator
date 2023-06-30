
from montecarlo.iteration import simulate_project_wip, work_work


def test_work_work():
    res_todo = work_work(todo=10, capacity=5)
    assert res_todo == 5

    res_todo = work_work(todo=4, capacity=5)
    assert res_todo == 0

    res_todo = work_work(todo=0, capacity=-1)
    assert res_todo == 0

def test_simulate_project_wip():
    from montecarlo.capacity import normal_generator
    import random
    random.seed(123)

    it, prog = simulate_project_wip(15, normal_generator(15, 1))

    assert it == [0, 1, 2]
    assert prog == [0, 15, 0.0]

    it, prog = simulate_project_wip(15, normal_generator(15, 1/3))

    assert it == [0, 1, 2, 3]
    assert prog == [0, 15, 9.070000135258464, 0]