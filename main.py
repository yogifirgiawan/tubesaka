import sys
import insertionSort
import List
import timeit
import execution
import time

if __name__ == "__main__":
    sys.setrecursionlimit(5000)
    if len(sys.argv) == 2:
        ldata = ["100DataTerbalik.txt","100DataUrut.txt"]
        for i in ldata:
            print("=========================")
            print("WORST CASE") if i == "100DataTerbalik.txt" else print("BEST CASE")
            arr = List.LoadList(i)
            print("Banyak data : {}".format(len(arr)))

            # iterative section
            start = timeit.default_timer()
            insertionSort.insertionSortIterative(arr)
            execution.calulate("Iterative selection sort", start)

            # recursive section
            arr = List.LoadList(i)
            start = timeit.default_timer()
            insertionSort.insertionSortRecursive(arr,0)
            execution.calulate("Recursive selection sort", start)
    else:
        ldata = ["100Data.txt","400Data.txt","1000Data.txt", "1500Data.txt"]
        for i in ldata:
            print("=========================")
            arr = List.LoadList(i)
            print("Banyak data : {}".format(len(arr)))

            # iterative section
            start = timeit.default_timer()
            insertionSort.insertionSortIterative(arr)
            
            execution.calulate("Iterative selection sort", start)

            # recursive section
            arr = List.LoadList(i)
            start = timeit.default_timer()
            insertionSort.insertionSortRecursive(arr,0)
            execution.calulate("Recursive selection sort", start)
