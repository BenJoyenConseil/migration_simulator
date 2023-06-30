import random
from montecarlo.migration import simulator
import numpy as np

def test_simulator():
    np.random.seed(123)
    runs = 100
    
    durations, workloads, progress = simulator(
        runs=runs, 
        stream_num=4, 
        stream_workload=1, 
        workload_disturb=1.4,
        people=5
    )

    assert np.histogram(workloads, bins=[0, 1, 2, 3])[0].tolist() == [206, 106, 45]
    assert np.average(workloads) == 1.3612425940303106
    assert np.median(workloads) == 0.9493946174728486
    assert round(np.sum(workloads) / runs) == 5

    assert np.percentile(durations, 75) == 6.

    assert progress[0] == {
        "iterations": [0, 1, 2, 3, 4],
        "progress": [0, 3.6232803433237253, 3.3538809332847217, 2.086608770235758, 0]
    }