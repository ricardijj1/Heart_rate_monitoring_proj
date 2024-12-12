def filter_nondigits(data: list) -> list:
    pass 
  
    new_list = []
    
    for x in data:

        if isinstance(x, str):
            x = x.strip()
            if x.isdigit():  
                x = int(x)
 
        if isinstance(x, int) and x != 0:
            new_list.append(x)
    
    return new_list
        
    
   
    """""
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """
 
def filter_outliers(data: list) -> list:
    
    outliers_list = []
    for y in data:
        if 30 < y < 250:
           outliers_list.append(y)
    

    return outliers_list


