import operator

def person_lister(f):
    def inner(people):
        # complete the function
        res=sorted(people,key=lambda k:int(k[2]))
        return  (f(x) for x in res)

    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


    """
3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 300 F
"""

    # x = [
    #     ['4', '21', '1', '14', '2008-10-24 15:42:58'],
    #     ['3', '22', '4', '2somename', '2008-10-24 15:22:03'],
    #     ['5', '21', '3', '19', '2008-10-24 15:45:45'],
    #     ['6', '21', '1', '1somename', '2008-10-24 15:45:49'],
    #     ['7', '22', '3', '2somename', '2008-10-24 15:45:51']
    # ]
    #
    # from operator import itemgetter
    #
    # x.sort(key=itemgetter(1))
    #
    # from itertools import groupby
    #
    # y = groupby(x, itemgetter(1))
    #
    # for elt, items in groupby(x, itemgetter(1)):
    #     print(elt, items)
    #     for i in items:
    #         print(i)
    #
    #         21 < itertools._grouper
    #         object
    #         at
    #         0x511a0 >
    #         ['4', '21', '1', '14', '2008-10-24 15:42:58']
    #         ['5', '21', '3', '19', '2008-10-24 15:45:45']
    #         ['6', '21', '1', '1somename', '2008-10-24 15:45:49']
    #         22 < itertools._grouper
    #         object
    #         at
    #         0x51170 >
    #         ['3', '22', '4', '2somename', '2008-10-24 15:22:03']
    #         ['7', '22', '3', '2somename', '2008-10-24 15:45:51']