def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []

    # loop through the list
    for i in a:
        # if not in cache and not 0
        if i not in cache and i != 0:
            # add it to cache
            cache[i] = i
            # check if the negative number is in the cache
            if -i in cache:
                # add it to the result but use abs (absolute value) so it turns positive
                result.append(abs(i))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
