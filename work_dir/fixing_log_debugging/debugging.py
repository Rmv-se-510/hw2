import logging, sys
logging.basicConfig(filename='partial_debugging.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.debug("NEW LOG")


def selectionSort(arr):
   logger = logging.getLogger(__name__)
   n = len(arr)
   for i in range(n):
       lowestIndex = i
       for j in range(n):
           if arr[j] < arr[lowestIndex]:
               lowestIndex = j


       logger.debug("lowest index: %r", lowestIndex) # what index contains the lowest value?
       logger.debug("i: %r", i) # where in the array should the ith smallest value be?
       logger.debug("n: %r", n) # where are we considering the end of the array?


       lowestNum = arr[lowestIndex]


       logger.debug("lowestNum: %r",lowestNum) # lowest number found in unsorted array


       logger.debug("before: %r", arr) # array state before we swap anything
       arr[lowestIndex] = arr[i]
       logger.debug("first: %r", arr) # array state after the first change
       arr[i] = lowestNum


       logger.debug("final: %r", arr) # array state after the second change
       n = n - 1


   return arr

arr_in = [5, 3, 2, 1, 8, 10, 11, 9, 23]

arr_out = selectionSort(arr_in)

print(arr_out)