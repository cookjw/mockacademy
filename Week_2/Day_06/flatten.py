# from http://stackoverflow.com/questions/406121/flattening-a-shallow-list-in-python?lq=1

def flatten(x):
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result