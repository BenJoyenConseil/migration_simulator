import random
from montecarlo.migration import simulator
import numpy as np

def test_simulator():
    np.random.seed(123)
    runs = 100
    
    result = simulator(
        runs=runs, 
        stream_num=4, 
        stream_workload=1, 
        workload_disturb=1.4,
        people=5
    )

    assert np.histogram(result["r_workloads"], bins=[0, 1, 2, 3])[0].tolist() == [206, 106, 45]
    assert np.average(result["r_workloads"]) == 1.3612425940303106
    assert np.median(result["r_workloads"]) == 0.9493946174728486
    assert round(np.sum(result["r_workloads"]) / runs) == 5

    assert np.percentile(result["r_durations"], 75) == 6.

    assert result["r_progress_by_run"][0] == {
        "iterations": [0, 1, 2, 3, 4],
        "progress": [0, 3.6232803433237253, 3.3538809332847217, 2.086608770235758, 0]
    }