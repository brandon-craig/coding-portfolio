import collections
import functools

	'''Decorator copied from the Python Decorator Library
	Found at: http://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
	Allows for partial computations to be cached so there is no 
	identical computation that is computed more than once. 
	'''
class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned 
    (not reevaluated).
     '''
    def __init__(self, func):
   		self.func = func
   		self.cache = {}
    def __call__(self, *args):
        try:
           return self.cache[args]
        except KeyError:
           value = self.func(*args)
           self.cache[args] = value
           return value
        except TypeError:
           # uncachable -- for instance, passing a list as an argument.
           # Better to not cache than to blow up entirely.
           return self.func(*args)
    def __repr__(self):
       '''Return the function's docstring.'''
       return self.func.__doc__
    def __get__(self, obj, objtype):
       '''Support instance methods.'''
       return functools.partial(self.__call__, obj)

class Knapsack:
	def __init__(self, items, weight):
		self.items = items
		self.maxWeight = weight

	@memoized
	def computeMaxSubseq(self, i, j):
		if i == 0:
			return 0

		v, w = self.items[i - 1]
		if w > j:
			return self.computeMaxSubseq(i - 1, j)

		else:
			return max(self.computeMaxSubseq(i - 1, j), self.computeMaxSubseq(i - 1, j - w) + v)

	def solveKnapsack(self):
		j = self.maxWeight
		resultSet = []

		for i in xrange(len(self.items), 0, -1):
			if self.computeMaxSubseq(i, j) != self.computeMaxSubseq(i - 1, j):
				resultSet.append(self.items[i - 1])
				j -= self.items[i - 1][1]

		resultSet.reverse()
		return self.computeMaxSubseq(len(self.items), self.maxWeight), resultSet