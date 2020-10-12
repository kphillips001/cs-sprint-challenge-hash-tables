def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    #create cache
    cache = {}

    if len(weights) < 2:
        return None
    
    #index of weights stored as values in cache starting at 0
    index = 0
    #loop through array of weights
    for weight in weights:
        # check if already in cache
        if (limit - weight) in cache:
            # if found return the index we're on
            return (index, cache[(limit - weight)])
        # if not in cache, add weight/index to it
        cache[weight] = index
        index += 1