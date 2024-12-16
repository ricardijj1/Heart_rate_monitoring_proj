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
    for x in range(0, len(data), n):
        window = data[x: x + n]
        maximums.append(max(window))  
    
    
   
    return maximums    
    ...

#function calculate the average in a window of  data 

def window_average(data: list, n: int) -> list:

    average_list= []
    for y in range(0, len(data), n):

#window range for each loop 
        window = data[y:y + n] 

#calculate average
        average = sum(window) / len(window)

#append average to empty list 
        average_list.append((round(average,2)))
    return average_list

import statistics

#function calculate standard deviation of a list 

def window_stddev(data: list, n: int) -> list:

    stddev_list = []

#loop going throught data 

    for a in range(0, len(data), n):
        window = data[a:a + n] 
        
        if len(window) <= 1:
            continue
#results appeneded to empty list 
        else:
            stnd = statistics.stdev(window)
            stddev_list.append(round(stnd,2))

    return stddev_list

        
    
    
        
            
    
        
    
        
    
    
    


