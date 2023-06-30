import numpy as np
import matplotlib.pyplot as plt

def describe(simulation_result):
    duration_avg = round(np.average(simulation_result["r_durations"]))
    duration_75pct = round(np.percentile(simulation_result["r_durations"], 75))
    duration_med = np.median(simulation_result["r_durations"])
    workload_med = np.median(simulation_result["r_workloads"])
    print(f"avg duration {duration_avg}, ",
          f"median duration {duration_med}, ",
          f"75pct duration {duration_75pct}, ",
          f"median stream workload {workload_med}")
    return duration_avg, duration_75pct, duration_med, workload_med


def plot(simulation_result):
    _, duration_75pct, duration_med, _ = describe(simulation_result)
    px = 1/plt.rcParams['figure.dpi']  # pixel in inches
    fig, (ax1, ax2) = plt.subplots(ncols=2, layout="constrained", figsize=(1500*px, 500*px))
    for p in simulation_result['r_progress_by_run']:
        ax1.plot(p['iterations'], p['progress'])
        ax2.hist(simulation_result['r_workloads'])
    ax1.set_xlabel('mois')
    ax1.set_ylabel('charge de travail')
    ax1.set_ylim([-3, None])
    ax1.set(title=f"""Pour {simulation_result['p_stream_num']} flux, la migration a 75% 
            de chance d'être terminée au bout de {duration_75pct} mois 
            (mediane-{simulation_result['p_runs']/2} : {duration_med} mois)""")
    plt.show()