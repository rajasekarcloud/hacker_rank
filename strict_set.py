'''You are given a set  and  other sets.
Your job is to find whether set  is a strict superset of each of the  sets.

Print True, if  is a strict superset of each of the  sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.
Example: If set A is {1, 2, 3, 4, 5} and set B is {2, 4}, then set B is a strict superset of set A because it contains all the elements of set A, but also has at least one element that is not in set A.

'''
from pandas.tseries.frequencies import is_superperiod

# Read main set
def strict_superset(input_set):
    result = [];
    how_many_subet = int(input());
    for _ in range(how_many_subet):
        sub_set = set(input().split());
        if input_set.issuperset(sub_set) !=True:
            result.append(False);
        else:
            result.append(True);
    if False in result:
        print(False);
    else:
        print(True);

if __name__ == '__main__':
    input_set = set(input().split());
    strict_superset(input_set);
