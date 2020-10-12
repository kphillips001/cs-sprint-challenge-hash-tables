#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # create cache and trip list to populate
    cache = {}
    trips = [None] * length

    # cache all the tickets as (source:destination)
    for t in tickets:
        cache[t.source] = t.destination

    # first flight is initiated with key None
    current = cache["NONE"]

    for i in range(length):
        # set trip index & store cache at current
        trips[i] = current
        # move pointer current in cache to next trip
        current = cache[current]

    return trips