from montecarlo import capacity
import random

def test_normal():
    random.seed(123)
    fibonacci = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    res = []
    
    for f in fibonacci:
        res.append(capacity.normal(f))

    assert round(sum(res) / len(res), 2) == 2.98

def test_wrapper():
    random.seed(123)

    res = capacity.normal_generator(34, 1/3)()

    assert res == 7.291046617241429