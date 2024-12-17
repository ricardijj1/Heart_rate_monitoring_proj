import statistics 

def window_max(data: list, n: int) -> list:
    """
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    """
    maximums = []

    #loop going through range of data to calculta maxim value
    for maxx in range(0, len(data), n):
        window = data[maxx: maxx + n]
        maximums.append(max(window))  
    return maximums    
    ...



def window_average(data: list, n: int) -> list:
    """
    Calculate average value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of averages from each window (size should be len(data)//6)
    """
    average_list= []
    for averages in range(0, len(data), n):

#window range for each loop 
        window = data[averages: averages + n] 

#calculate average
        average = sum(window) / len(window)

#append average to empty list 
        average_list.append((round(average,2)))
    return average_list





def window_stddev(data: list, n: int) -> list:
    """
    Calculate standard deviation value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of standard deviation values from each window (size should be len(data)//6)
    """
    stddev_list = []
#loop going throught data 
    for stds in range(0, len(data), n):
        window = data[stds:stds + n] 
        
        if len(window) <= 1:
            continue
#results appeneded to empty list 
        else:
            stnd = statistics.stdev(window)
            stddev_list.append(round(stnd,2))

    return stddev_list

        
    
    
        
            
    
        
    
        
    
    
    


