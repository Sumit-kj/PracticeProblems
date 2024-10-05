def are_two_arrays_same(arr_1, arr_2):
    """
    This function checks if the two arrays are same or not
    :param arr_1: First array to be compared
    :param arr_2: Second array to be compared
    :return: Boolean if
    """
    if len(arr_1) != len(arr_2):
        return False

    arr_1.sort()
    arr_2.sort()
    n = len(arr_1)
    for i in range(n):
        el_1 = arr_1[i]
        el_2 = arr_2[i]

        if type(el_1) is not type(el_2):
            return False

        if type(el_1) is list:
            el_1.sort()
            el_2.sort()
            if el_1 != el_2:
                return False

        else:
            if el_1 != el_2:
                return False

    return True
