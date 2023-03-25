#!/usr/bin/env python

import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from sorting_algorithms_generators import *

def run_animation(sorting_algorithm, size_of_dataset, interval):
    
    def frame_generator():
        nonlocal data
        yield from sorting_algorithm(data)

    def animation(frame):
        nonlocal colors, data, previous_active_index
        data, active_index = frame

        if active_index == -1:
            colors = [finished_color for i in range(len(data))]
        else:
            colors[previous_active_index] = inactive_color
            colors[active_index] = active_color
            previous_active_index = active_index

        ax.cla()
        ax.bar(x, data, color=colors)


    # data preparation
    data = [i + 1 for i in range(size_of_dataset)]
    x = data.copy()
    random.shuffle(data)

    inactive_color = "#1f77b4"
    active_color = "#ff7f0e"
    finished_color = "#2ca02c"
    previous_active_index = 0
    colors = [inactive_color for _ in range(len(data))]


    fig, ax = plt.subplots()
    ax.tick_params(
        bottom=False,
        top=False,
        left=False,
        right=False,
        labelbottom=False,
        labelleft=False
    )

    ani = FuncAnimation(fig, animation, interval=interval, frames=frame_generator, repeat=False, cache_frame_data=False)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Sorting algorithm visualisation"
    )
    parser.add_argument("algorithm",
                        help="Can be one of: insertion/selection/bubble/merge/heap",
                        type=str)
    
    algorithms = {
        "insertion": insertion_sort,
        "selection": selection_sort,
        "bubble": bubble_sort,
        "merge": merge_sort,
        "heap": heap_sort,
    }

    args = parser.parse_args()
    if args.algorithm not in algorithms.keys():
        print("Error: Invalid argument. Valid arguments are:")
        print("    insertion")
        print("    selection")
        print("    bubble")
        print("    merge")
        print("    heap")
        exit(1)

    run_animation(algorithms[args.algorithm], 60, 40) 
