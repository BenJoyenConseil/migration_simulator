
from montecarlo.iteration import simulate_project_wip, capacity
import numpy as np

xp_variables = {
    "runs": 100,
    "stream_num": 13,
    "stream_workload": 1,
    "workload_disturb": 1.2,
    "people": 13,
    "capacity_rate": 1/3
}

def simulator(runs=1000, 
              stream_num=13, 
              stream_workload=1, 
              workload_disturb=1.2, 
              people=13, 
              capacity_rate=1/3):
    durations = []
    workloads = []
    progress_by_run = []
    for i in range(0, runs):
        gamma_todo = np.random.gamma(stream_workload, workload_disturb, stream_num)
        iterations, todo_progress = simulate_project_wip(
            todo=gamma_todo.sum(),
            capacity_generator=capacity.normal_generator(people, capacity_rate)
        )
        durations.append(iterations[-1])
        workloads += gamma_todo.tolist()
        progress_by_run.append({
            "iterations": iterations,
            "progress": todo_progress
        })
    
    return {
        "p_runs": runs,
        "p_stream_num": stream_num,
        "p_stream_workload": stream_workload,
        "p_workload_disturb": workload_disturb,
        "p_people": people,
        "p_capacity_rate": capacity_rate, 
        "r_durations": durations, 
        "r_workloads": workloads, 
        "r_progress_by_run": progress_by_run
    }