def binary_search(target, sorted_list):
    """
    Takes a target value and a sorted list as input
    Returns the position (index) of the target in the sorted list
    """

    low, high = 0, len(sorted_list)-1

    while low <= high:
        mid = (low+high)//2

        guess = sorted_list[mid]

        if guess == target:
            return mid
        elif guess < target:
            low = mid+1
        else:
            high = mid-1