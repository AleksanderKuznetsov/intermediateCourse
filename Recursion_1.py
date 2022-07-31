"""
Raising the number N to the power M.
"""


def degree(N, M):
    """
    :param N: number.
    :param M: degree.
    """
    if M == 0:
        return 1
    return degree(N, M-1) * N
