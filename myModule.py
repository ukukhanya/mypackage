def top_n(items, n):
    """Return the top n items in an array in descending order
    
    Args:
    items (array): list or array-like object
    n (int): number of items to return
    
    Return:
    array: top n items in descending order
    
    Example:
    >> top_n([8, 2, 3, 7, 4], 3)
    [8, 7, 4]"""

    sorted_list = items.sort(reverse = True)
    return sorted_list[:n]