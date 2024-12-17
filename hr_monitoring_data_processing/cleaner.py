def filter_nondigits(data: list) -> list:

    """""
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """
    new_list = []
    for datas in data:
    #taking string and striping out new lines and turning data into intergers 
        if isinstance(datas, str):
            datas = datas.strip()
            if datas.isdigit():  
                datas = int(datas)
    #appending all intergers into new list 
        if isinstance(datas, int) and datas != 0:
            new_list.append(datas)
    return new_list


def filter_outliers(data: list) -> list:
    """""
    Filter all outliers that fall out the range of our data from list the new list of just intergers
    Args:
        data (list[str]): list of interger representing heart rate samples.
            
    Returns:
        list[int]: list of integers, the fit within the range we want.
    """
    
    outliers_list = []
    for liers in data:
    #looping through data and appending intergers are less than 30 and less than 250
        if 30 < liers < 250:
           outliers_list.append(liers)
    #new list with outliers removed is returned 
    return outliers_list


