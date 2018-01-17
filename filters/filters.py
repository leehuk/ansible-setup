## ansible_filter::getkeys
##   Provides helper functions for getting key values from dictionaries
##
class FilterModule(object):
    def filters(self):
        return {
            'getkeys': getkeys,
            'getkeys_or': getkeys_or,
        }

def getkeys(data, keys):
    """Locate values within data where all keys are present

    :param data: Data to search, in list of dict form [{...},{...}]
    :param keys: Keys to search for, in string '...' or list form ['...','...']
    :returns:    Results from data with all keys present, in list of dict form [{...},{...}]
                 Note: Only returns matching key-value pairs, not other unmatched data
    """
    if not isinstance(keys, list):
        keys = [keys]

    results = []
    for entry in data:
        result = {}
        missing = False

        for key in keys:
            if key in entry:
                result[key] = entry[key]
            else:
                missing = True

        if missing == False:
            results.append(result)

    return results

def getkeys_or(data, keys):
    """Locate values within data where any keys are present

    :param data: Data to search, in list of dict form [{...},{...}]
    :param keys: Keys to search for, in string '...' or list form ['...','...']
    :returns:    Values of matching keys, in list form [value,value]
    """
    if not isinstance(keys, list):
        keys = [keys]

    results = []
    for entry in data:
        for key in keys:
            if key in entry:
                results.append(entry[key])

    return results
