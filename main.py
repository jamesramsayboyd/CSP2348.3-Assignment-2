import random
import time


""" Generates an array of random numbers between 0 and 99. Array size is chosen by the user. """
def generate_random_integer_set(a):
    array = []
    for i in range(a):
        array.append(random.randint(0, 999))
    return array


def selection_sort(array):
    arr = array[:] # creating a copy of the array to preserve the original
    comparison_counter = copy_counter = 0
    timer_start = time.perf_counter_ns()
    n = len(arr)
    for i in range(n):
        minimum = i
        for j in range(i + 1, n):
            comparison_counter += 1
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]
        copy_counter += 2
    timer_end = time.perf_counter_ns()
    return "Selection Sort", n, comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


def insertion_sort(array):
    arr = array[:] # creating a copy of the array to preserve the original
    comparison_counter = copy_counter = 0
    timer_start = time.perf_counter_ns()
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparison_counter += 1
            arr[j + 1] = arr[j]
            copy_counter += 1
            j -= 1
        arr[j + 1] = key
    timer_end = time.perf_counter_ns()
    return "Insertion Sort", n, comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


def merge_sort(array):
    arr = array[:] # creating a copy of the array to preserve the original
    print(arr)
    comparison_counter = copy_counter = 0
    timer_start = time.perf_counter_ns()
    n = len(arr)
    if len(arr) > 1:
        i = j = k = 0
        mid = len(arr) // 2
        sub_array_1 = arr[:mid]
        sub_array_2 = arr[mid:]

        merge_sort(sub_array_1)
        merge_sort(sub_array_2)

        while i < len(sub_array_1) and j < len(sub_array_2):
            if sub_array_1[i] < sub_array_2[j]:
                comparison_counter += 1
                arr[k] = sub_array_1[i]
                copy_counter += 1
                i += 1
            else:
                comparison_counter += 1
                arr[k] = sub_array_2[j]
                copy_counter += 1
                j += 1
            k += 1

        while i < len(sub_array_1):
            arr[k] = sub_array_1[i]
            copy_counter += 1
            i += 1
            k += 1

        while j < len(sub_array_2):
            arr[k] = sub_array_2[j]
            copy_counter += 1
            j += 1
            k += 1

    timer_end = time.perf_counter_ns()
    print(arr)
    return "Merge Sort", n, comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


def quick_sort_partition(arr, low, high):
    #arr = array[:]  # creating a copy of the array to preserve the original
    comparison_counter = copy_counter = 0
    timer_start = time.perf_counter_ns()

    # choose the rightmost element as pivot
    pivot = arr[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (arr[i], arr[j]) = (arr[j], arr[i])

    # Swap the pivot element with the greater element specified by i
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    # Return the position from where partition is done
    return i + 1


def quick_sort(array, low, high):
    arr = array[:]  # creating a copy of the array to preserve the original
    #print(arr)
    comparison_counter = copy_counter = 0
    timer_start = time.perf_counter_ns()
    n = len(arr)
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = quick_sort_partition(arr, low, high)

        # Recursive call on the left of pivot
        quick_sort(arr, low, pi - 1)

        # Recursive call on the right of pivot
        quick_sort(arr, pi + 1, high)
    timer_end = time.perf_counter_ns()
    #print(arr)
    return "Quick Sort", n, comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


def heapify(arr, n, i):
    comparison_counter = copy_counter = 0
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        comparison_counter += 1
        arr[i], arr[largest] = arr[largest], arr[i]
        copy_counter += 1
        results = heapify(arr, n, largest)
        comparison_counter += results[0]
    return comparison_counter, copy_counter


def heap_sort(array):
    arr = array[:] # creating a copy of the array to preserve the original
    #print(arr)
    comparison_counter = copy_counter = 0
    timer_start = time.perf_counter_ns()
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        results = heapify(array, n, i)
        comparison_counter += results[0]
        copy_counter += results[1]

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        copy_counter += 1
        results = heapify(arr, i, 0)
        comparison_counter += results[0]
        copy_counter += results[1]

    timer_end = time.perf_counter_ns()
    #print(arr)
    return "Heap Sort", n, comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


def bubble_sort(array):
    arr = array[:] # creating a copy of the array to preserve the original
    comparison_counter = copy_counter = 0
    timer_start = time.perf_counter_ns()
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1):
            comparison_counter += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap adjacent elements
                copy_counter += 1
    timer_end = time.perf_counter_ns()
    return "Bubble Sort", n, comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


def obs1_bubble_sort(array):
    arr = array[:] # creating a copy of the array to preserve the original
    comparison_counter = copy_counter = 0
    timer_start = time.perf_counter_ns()
    n = len(arr)
    for i in range(n - 1):
        for k in range(0, n - i - 1):
            comparison_counter += 1
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]  # swap adjacent elements
                copy_counter += 1
    timer_end = time.perf_counter_ns()
    return "Obs1 Bubble Sort", n, comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


def obs2_bubble_sort(array):
    arr = array[:] # creating a copy of the array to preserve the original
    comparison_counter = copy_counter = 0
    timer_start = time.perf_counter_ns()
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for k in range(n - 1):
            comparison_counter += 1
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]  # swap adjacent elements
                copy_counter += 1
                swapped = True
        if not swapped:
            break
    timer_end = time.perf_counter_ns()
    return "Obs2 Bubble Sort", n, comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


def obs3_bubble_sort(array):
    arr = array[:] # creating a copy of the array to preserve the original
    comparison_counter = copy_counter = 0
    timer_start = time.perf_counter_ns()
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for k in range(n - i - 1):
            comparison_counter += 1
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]  # swap adjacent elements
                copy_counter += 1
                swapped = True
        if not swapped:
            break
    timer_end = time.perf_counter_ns()
    return "Obs3 Bubble Sort", n, comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


def sink_down_sort(array):
    arr = array[:] # creating a copy of the array to preserve the original
    comparison_counter = copy_counter = 0
    timer_start = time.perf_counter_ns()
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for k in reversed(range(n - i - 1)):
            comparison_counter += 1
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]  # swap adjacent elements
                copy_counter += 1
                swapped = True
        if not swapped:
            break
    timer_end = time.perf_counter_ns()
    return "Sink-Down Sort", n, comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


def bi_directional_bubble_sort(array):
    arr = array[:] # creating a copy of the array to preserve the original
    comparison_counter = copy_counter = 0
    timer_start = time.perf_counter_ns()
    n = len(arr)
    array_sorted = False
    while not array_sorted:
        array_sorted = True
        for i in (range(n - 1)):
            comparison_counter += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                copy_counter += 1
                array_sorted = False
        if array_sorted:
            break

        array_sorted = True
        for i in reversed(range(n - 1)):
            comparison_counter += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                copy_counter += 1
                array_sorted = False
        if array_sorted:
            break
    timer_end = time.perf_counter_ns()
    return "BD Bubble Sort", n, comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


""" Calls the appropriate sorting algorithm function and passes it an array of the user's chosen size. Returns five
relevant data points as a list, i.e.
result[0] = The sorting algorithm's name
result[1] = The size of the array
result[2] = Number of comparison operations performed
result[3] = Number of copy operations performed
result[4] = Time taken (in ms.)
"""
def test_single_algorithm(choice, array):
    if choice == 1:
        return selection_sort(array)
    elif choice == 2:
        return insertion_sort(array)
    elif choice == 3:
        return merge_sort(array)
    elif choice == 4:
        return quick_sort(array, 0, len(array) - 1)
    elif choice == 5:
        return heap_sort(array)
    elif choice == 6:
        return bubble_sort(array)
    elif choice == 7:
        return obs1_bubble_sort(array)
    elif choice == 8:
        return obs2_bubble_sort(array)
    elif choice == 9:
        return obs3_bubble_sort(array)
    elif choice == 10:
        return sink_down_sort(array)
    elif choice == 11:
        return bi_directional_bubble_sort(array)
    else:
        print("Error: Invalid input")


""" Prompts the user to choose a sorting algorithm and an input size, before generating an array of random numbers and
sending it to the appropriate sorting function. Data is passed to the table_formatter function for printing to the
console as a table.
"""
def print_single_algorithm_test_results(data_set):
    column_headers = [["Algorithm Name", "Array Size", "No. of Comparisons", "Run Time (in ms.)"]]
    table_data = [[data_set[0], data_set[1], data_set[2], data_set[4]]]
    print("Testing", data_set[0], "algorithm with input size: ", data_set[1])
    table_formatter(column_headers, table_data)


""" Prompts the user for an input size, then generates an array of random numbers and passes this single array to each
of the 11 sorting algorithms to compare results. Data is sent to the table_formatter function to be printed as a table.
"""
def print_multiple_algorithm_test_results(input_size):
    array = generate_random_integer_set(input_size)
    column_headers = [["Algorithm Name", "Array Size", "No. of Comparisons", "Run Time (in ms.)"]]
    table_data = []
    for i in range(11):
        data_set = test_single_algorithm(i + 1, array)
        table_data.append([data_set[0], data_set[1], data_set[2], data_set[4]])
    table_formatter(column_headers, table_data)


""" Generates Table 2 from the assignment document, comparing the number of comparison operations performed by each
sorting algorithm. Uses three nested loops to iterate through 11 sorting algorithms, 6 different input sizes and 10 
tests each, taking the average of each test for each input size for each algorithm. Passes all this data to the 
table_formatter function for printing to the console.
"""
def print_table_two():
    print("Generating Table 2 (this may take up to 30 seconds)...")
    print("\nAverage number of comparisons for sorting arrays of n integers (over 10 runs)")
    column_headers = [["Sorting Algorithm", "n = 100", "n = 200", "n = 400", "n = 800", "n = 1000", "n = 2000"]]
    input_size = [100, 200, 400, 800, 1000, 2000] # size of arrays to generate for testing
    all_data = [] # initialising lists to store data
    for i in range(11): # no. of sorting algorithms
        row_of_averages = [] # list to store averages data for various input sizes
        for x in input_size: # 100, 200, 400, etc
            comparison_counter = 0 # resetting comparison counter for each test
            for j in range(10): # no of tests to perform to find average
                array = generate_random_integer_set(x) # generate random number set of 100, 200, etc
                result = test_single_algorithm(i + 1, array) # storing results
                comparison_counter += result[2] # counting no. of comparisons
            avg_comparisons = comparison_counter // 10 # finding average no. of comparisons by dividing by no. of tests
            row_of_averages.append(avg_comparisons) # adding average no. of comparisons to list
        row_of_averages.insert(0, result[0]) # inserting name of sorting algorithm to first index of list
        all_data.append(row_of_averages) # appending entire list with algorithm name and averages of all tests to final list
    table_formatter(column_headers, all_data) # feeding data to table_formatter function


""" Generates Table 3 from the assignment document, comparing the time taken by each of the 11 sorting algorithms. 
Uses three nested loops to iterate through 11 sorting algorithms, 6 different input sizes and 10 tests each, taking the 
average of each test for each input size for each algorithm. Passes all this data to the table_formatter function for 
printing to the console.
"""
def print_table_three():
    print("Generating Table 3 (this may take up to 30 seconds)...")
    print("\nAverage time taken for sorting arrays of n integers (over 10 runs, displayed in ms)")
    column_headers = [["Sorting Algorithm", "n = 100", "n = 200", "n = 400", "n = 800", "n = 1000", "n = 2000"]]
    input_size = [100, 200, 400, 800, 1000, 2000]  # size of arrays to generate for testing
    all_data = []  # initialising lists to store data
    for i in range(11):  # no. of sorting algorithms
        row_of_averages = []  # list to store averages data for various input sizes
        for x in input_size:  # 100, 200, 400, etc
            time_counter = 0  # resetting time counter for each test
            for j in range(10):  # no of tests to perform to find average
                array = generate_random_integer_set(x)  # generate random number set of 100, 200, etc
                result = test_single_algorithm(i + 1, array)  # storing results
                time_counter += result[4]  # counting total time taken
            avg_time = round(time_counter / 10, 2)  # finding average time by dividing by no. of tests, round to 2dp
            row_of_averages.append(avg_time)  # adding average time to list
        row_of_averages.insert(0, result[0])  # inserting name of sorting algorithm to first index of list
        all_data.append(
            row_of_averages)  # appending entire list with algorithm name and averages of all tests to final list
    table_formatter(column_headers, all_data) # feeding data to table_formatter function


""" A function used to print data in a nicely formatted data. Takes two lists as arguments, one for column headers
and one for data in each row
"""
def table_formatter(column_headers, test_data):
    format_row = "{:^20}" * len(column_headers[0])
    for x in column_headers:
        print(format_row.format(*x))
    for row in test_data:
        print(format_row.format(*row))


def main():
    while True:
        print("1. Test an individual sorting algorithm\n2. Test multiple sorting algorithms\n"
              "3. Generate Table 2\n4. Generate Table 3\n5. Exit")
        print()
        user_choice = int(input("Enter choice: "))

        if user_choice == 1:
            print("1. Selection Sort\n2. Insertion Sort\n3. Merge Sort\n4. Quick Sort\n5. Heap Sort\n"
                  "6. Bubble Sort\n7. Obs1 Bubble Sort\n8. Obs2 Bubble Sort\n9. Obs3 Bubble Sort\n"
                  "10. Sink-Down Sort\n11. Bi-Directional Sort")
            print()
            algo_choice = int(input("Enter choice: "))
            array_size = int(input("Enter an array size: "))
            array = generate_random_integer_set(array_size)
            print_single_algorithm_test_results(test_single_algorithm(algo_choice, array))
            print()
        elif user_choice == 2:
            array_size = int(input("Enter an array size: "))
            print_multiple_algorithm_test_results(array_size)
            print()
        elif user_choice == 3:
            print_table_two()
            print()
        elif user_choice == 4:
            print_table_three()
            print()
        elif user_choice == 5:
            print("Goodbye")
            break
main()
