from itertools import combinations

def maximal_compatible_subsets(X, bin_rel):
    retval = []
    for i in range(len(X) + 1, 1, -1):
        for j in combinations(X, i):
            if all(bin_rel(a, b) for a, b in combinations(j, 2)) and not any(set(j).issubset(a) for a in retval):
                retval.append(tuple(j))
    return tuple(retval)

if __name__ == '__main__':
    x = ( (1,2,3), (1,3), (1,6), (3,4), (3,5), (4,5) )

    def nonempty_intersection(a, b):
        return set(a).intersection(b)

    print x
    print maximal_compatible_subsets(x, nonempty_intersection)
