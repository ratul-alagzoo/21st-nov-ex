import cProfile
import pstats
from sorts import quicksort, quicksort_inplace, insertionsort, test_sorted

if __name__ == "__main__":
    cProfile.run("test_sorted(quicksort)", "quicksort_cpu.prof")

    cProfile.run("test_sorted(quicksort_inplace)", "quicksort_inplace_cpu.prof")

    cProfile.run("test_sorted(insertionsort)", "insertionsort_cpu.prof")