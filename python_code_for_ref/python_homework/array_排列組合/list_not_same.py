import itertools 
print (list(itertools.permutations([1,2,3,4],3)))

''' 
import itertools 
>>> print list(itertools.permutations([1,2,3,4],2)) 
[(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)] 
 
>>> print list(itertools.combinations([1,2,3,4],2)) 
[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)] 
'''