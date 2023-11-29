def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    i = 0
    mx = data[i]
    while i < len(data):
        
        if mx < data[i]:
            mx = data[i]
        i += 1
    return data.count(mx)