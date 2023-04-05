import random
import time


def generate_random_integer_set(a):
    array = []
    for i in range(a):
        array.append(random.randint(0, 99))
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
            comparison_counter += 1
            if sub_array_1[i] < sub_array_2[j]:
                arr[k] = sub_array_1[i]
                copy_counter += 1
                i += 1
            else:
                arr[k] = sub_array_2[j]
                copy_counter += 1
                j += 1
            k += 1

        while i < len(sub_array_1):
            comparison_counter += 1
            arr[k] = sub_array_1[i]
            copy_counter += 1
            i += 1
            k += 1

        while j < len(sub_array_2):
            comparison_counter += 1
            arr[k] = sub_array_2[j]
            copy_counter += 1
            j += 1
            k += 1

    timer_end = time.perf_counter_ns()
    return "Merge Sort", n, comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


def quick_sort_partition(array, low, high):
    arr = array[:]  # creating a copy of the array to preserve the original
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
    return "Quick Sort", n, comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


def heapify(array, n, i):
    arr = array[:]
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(array):
    arr = array[:] # creating a copy of the array to preserve the original
    comparison_counter = copy_counter = 0
    timer_start = time.perf_counter_ns()
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    timer_end = time.perf_counter_ns()
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


def print_single_algorithm_test_results(data_set):
    column_headers = [["Algorithm Name", "Array Size", "No. of Comparisons", "Run Time (in ms.)"]]
    table_data = [[data_set[0], data_set[1], data_set[2], data_set[4]]]
    table_formatter(column_headers, table_data)


def print_multiple_algorithm_test_results(input_size):
    array = generate_random_integer_set(input_size)
    column_headers = [["Algorithm Name", "Array Size", "No. of Comparisons", "Run Time (in ms.)"]]
    table_data = []
    for i in range(11):
        data_set = test_single_algorithm(i + 1, array)
        table_data.append([data_set[0], data_set[1], data_set[2], data_set[4]])
    table_formatter(column_headers, table_data)


def find_average_comparison_number(array):
    comparison_counter = 0
    for i in range(10):
        comparison_counter += test_single_algorithm(1, array)[2]
        avg_comparisons = comparison_counter / 10
    return avg_comparisons



def print_table_two():
    input_size = [100, 200, 400, 800, 1000, 2000]
    comparison_counter = 0

    for x in input_size:
        array = generate_random_integer_set(x)
        for i in range(11):
            find_average_comparison_number(array)


    for i in range(10):
        data_set = test_single_algorithm(1, 100)

    # for i in input_size:
    #     for j in range(11):
    #         for k in range(10):
    #             comparison_counter += test_single_algorithm(j, i)[2]
    #             average_comparison = comparison_counter / i
    # for i in range(1, 12):
    #     for j in input_size:
    #         test_single_algorithm(i, j)
    # column_headers = [["Sorting Algorithm", "n=100", "n=200", "n=400", "n=800", "n=1000", "n=2000"]]



def print_table_three():
    column_headers = [["Sorting Algorithm", "n=100", "n=200", "n=400", "n=800", "n=1000", "n=2000"]]



def table_formatter(column_headers, test_data):
    print("Test Results:")
    for x in column_headers:
        print('| {:^20} | {:^20} | {:^20} | {:^20} |'.format(*x))
    for row in test_data:
        print('| {:^20} | {:^20} | {:^20} | {:^20} |'.format(*row))


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
            print("generating table 2")
        elif user_choice == 4:
            print("generating table 2")
        elif user_choice == 5:
            print("Goodbye")
            break
main()
