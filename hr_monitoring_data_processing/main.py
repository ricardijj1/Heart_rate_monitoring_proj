"""
The main Python mpdule that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import window_max, window_average, window_stddev
from cleaner import filter_nondigits, filter_outliers

import matplotlib.pyplot as plt




def run(filename: str) -> None: 
    """
    Process heart rate data from the specified file, clean it, calculate metrics, 
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/data1.txt').

    Steps:
        1. Read the file into a list of strings.
        2. Use `filter_nondigits` to clean the data and remove invalid entries.
        3. Use `filter_outliers` to remove unrealistic heart rate samples (<30 or >250).
        4. Calculate rolling maximums, averages, and standard deviations using functions from `metrics.py`.
        5. Save the plots to the `images/` folder:
            - Rolling maximums -> 'images/maximums.png'
            - Rolling averages -> 'images/averages.png'
            - Rolling standard deviations -> 'images/stdevs.png'

    Returns:
        list[int], list[int], list[int]: You will return the maximums, averages, and stdevs (in this order).
    """ 
    
    data = []
    file = open(filename)
    for line in file:
        data.append(line)
    file.close()
    data = filter_nondigits(data)
    data = filter_outliers(data)
    

    max_values= window_max(data, 6)

    average_values= window_average(data, 6)

    stnd_values = window_stddev(data, 6)

    fig, ax = plt.subplots()
    ax.plot(max_values)
    plt.savefig("images/averages.png")

    fig, ax = plt.subplots()
    ax.plot(stnd_values)
    plt.savefig("images/maximums.png")


    fig, ax = plt.subplots()
    ax.plot(stnd_values)
    plt.savefig("images/stdevs.png")
 # return all 3 lists
    return max_values, average_values, stnd_values
    

if __name__ == "__main__":
    run("data/data2.txt")
    
