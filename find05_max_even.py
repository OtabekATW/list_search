def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    i = 0
    mx_even = data[i]
    list1 = []

    while i < len(data):

        if data[i] % 2 == 0:
            list1.append(data[i])
        i += 1

    k = 0
    mx_even = list1[k]
    while k < len(list1):

        if mx_even < list1[k]:
            mx_even = list1[k]
        k += 1

    return mx_even