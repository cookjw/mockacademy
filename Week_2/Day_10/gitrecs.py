
#Code from Carl Meyer's PyCon 2013 talk on automated testing (suitably adapted)


# def similarity(watched1, watched2):
    # """
    # Return similarity score for two users.
    
    # Users represented as iterables of watched repo names.
    
    # Score is Jaccard index (intersection / union).
    
    # """
    # intersection = 0
    # for repo in watched1:
        # if repo in watched2:
            # intersection += 1
    # union = len(watched1) + len(watched2) - intersection
    
    # return float(intersection) / float(union) # Meyer is using Python 3, so he doesn't have to write "float".
    
# def similarity(watched1, watched2):
    # """
    # Return similarity score for two users.
    
    # Users represented as iterables of watched repo names.
    
    # Score is Jaccard index (intersection / union).
    
    # """

    # watched1, watched2 = set(watched1), set(watched2)
    # intersection = watched1.intersection(watched2)
    # union = watched1.union(watched2)

    # return float(len(intersection)) / float(len(union))



# def similarity(watched1, watched2):
    # """
    # Return similarity score for two users.
    
    # Users represented as iterables of watched repo names.
    
    # Score is Jaccard index (intersection / union).
    
    # """

    # watched1, watched2 = set(watched1), set(watched2)
    # intersection = watched1.intersection(watched2)
    # union = watched1.union(watched2)

    # # print "len(intersection): " + str(len(intersection))
    # # print "len(union): " + str(len(union))
    # # print len(intersection) / len(union)
    # return float(len(intersection)) / float(len(union))
    
    
def similarity(watched1, watched2):
    """
    Return similarity score for two users.
    
    Users represented as iterable of watched repos.
    
    Score is Jaccard index (intersection / union).
    """
    watched1, watched2 = set(watched1), set(watched2)
    intersection = watched1.intersection(watched2)
    union = watched1.union(watched2)
    
    if not union:
        return 0.0
    return float(len(intersection)) / float(len(union))
   