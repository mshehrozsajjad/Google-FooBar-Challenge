import random
import collections , itertools 

#Naiive Approach
def foo(L):
    assert 0 not in L
    A = 0
    for i,x in enumerate(L):
        for j,y in enumerate(L[i + 1:]):
            if not y % x:
                for k,z in enumerate(L[i + j + 2:]):
                    if  not z % y:
                        A = A + 1

    return A


#Very Fast Approach
def answer(lst):
    edges = [[] for _ in range(len(lst))]

    for i, j in itertools.combinations(range(len(lst)), 2):
        if lst[j] % lst[i] == 0:
            edges[i].append(j)
    return sum(len(edges[j]) for i in range(len(lst)) for j in edges[i])

#Compact Form of Fast Approach
def compact(lst):
	edges = [[j for j in range(i + 1, len(lst)) if lst[j] % lst[i] == 0] for i in range(len(lst))]
	return sum(len(edges[j]) for i in range(len(lst)) for j in edges[i])

#Generating a very large list to test
L = [random.randint(1, 999) for _ in range(1000)] 

#See Time Difference in both
print answer(L)
print compact(L)
print foo(L)

