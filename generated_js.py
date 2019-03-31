from pprint import pprint


def morris_graph(name, periods, keys, values):
    morris_area = {
        'element': name,
        'data': [],
        'xkey': 'period',
        'ykeys': keys,
        'labels': keys,
        'pointSize': 2,
        'hideHover': 'auto',
        'resize': 'true'
    }
    for i in range(len(periods)):
        iter_dict = {'period': periods[i]}
        for j in range(len(keys)):
            iter_dict[keys[j]] = values[i][j]
        morris_area['data'].append(iter_dict)
    return morris_area


#pprint(morris_graph('some_area', ['2010', '2011', '2012', '2013'], ['likes', 'follows'],
                    #[[10, 11], [21, 33], [234, 432], [3423, 2342]]))
