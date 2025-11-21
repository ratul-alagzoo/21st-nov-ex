from sorts import quicksort, quicksort_inplace, insertionsort, test_sorted

def run():
    test_sorted(quicksort)
    # test_sorted(quicksort_inplace)
    # test_sorted(insertionsort)

if __name__ == "__main__":

    # run time winner: quicksort_inplace()
    # memory winner: insertionsort()
    run()