def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    i = 0
    list1 = []
    while i < len(data):

        if data[i] % 2 == 0:
            list1.append(data[i])
        i += 1

    k = 0
    mn_even = list1[k]
    while k < len(list1):

        if list1[k] < mn_even:
            mn_even = list1[k]
        
        k += 1

    return mn_even
