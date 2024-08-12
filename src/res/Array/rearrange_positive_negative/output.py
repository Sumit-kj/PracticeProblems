o_p = [
    [9, -7, 8, -3, 5, -1, 2, 4, 6],
    [7, -2, 3, -5, -1, -4]
]


def validate_output(res):
    """
    This function validates the output, as the output can vary based on approaches taken
    """
    pos_count, neg_count, pair_count, extra_count, extra_type = 0, 0, 0, 0, 0
    for i in res:
        if i > 0:
            pos_count += 1
        else:
            neg_count += 1
    pair_count = pos_count if pos_count < neg_count else neg_count
    extra_count = abs(pos_count - neg_count)
    for i in range(pair_count):
        if res[i * 2] * res[i * 2 + 1] > 0:
            return -1
    if pos_count > neg_count:
        extra_type = 1
    else:
        extra_type = -1
    for i in range(1, extra_count + 1):
        if extra_type == 1 and res[-1 * i] < 0:
            return -1
        elif extra_type == -1 and res[-1 * i] > 0:
            return -1
    return 1
