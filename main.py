import random
import time


def generate_random_integer_set(a):
    array = []
    for i in range(a):
        array.append(random.randint(0, 99))
    return array


def selection_sort(arr):
    timer_start = time.perf_counter_ns()
    comparison_counter = copy_counter = 0
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
    return comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


def insertion_sort(arr):
    timer_start = time.perf_counter_ns()
    comparison_counter = copy_counter = 0
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
    return comparison_counter, copy_counter, timer_end - timer_start


def merge_sort(arr):
    if len(arr) > 1:
        timer_start = time.perf_counter_ns()
        comparison_counter = copy_counter = i = j = k = 0
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
        return comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


def quick_sort_partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


def quick_sort(array, low, high):
    timer_start = time.perf_counter_ns()
    comparison_counter = copy_counter = 0
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = quick_sort_partition(array, low, high)

        # Recursive call on the left of pivot
        quick_sort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, high)
    timer_end = time.perf_counter_ns()
    return comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


def heapify(arr, n, i):
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


def heap_sort(arr):
    timer_start = time.perf_counter_ns()
    comparison_counter = copy_counter = 0
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    timer_end = time.perf_counter_ns()
    return comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


def bubble_sort(arr):
    timer_start = time.perf_counter_ns()
    comparison_counter = copy_counter = 0
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1):
            comparison_counter += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap adjacent elements
                copy_counter += 1
    timer_end = time.perf_counter_ns()
    return comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


def obs1_bubble_sort(arr):
    timer_start = time.perf_counter_ns()
    comparison_counter = copy_counter = 0
    n = len(arr)
    for i in range(n - 1):
        for k in range(0, n - i - 1):
            comparison_counter += 1
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]  # swap adjacent elements
                copy_counter += 1
    timer_end = time.perf_counter_ns()
    return comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


def obs2_bubble_sort(arr):
    timer_start = time.perf_counter_ns()
    comparison_counter = copy_counter = 0
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
    return comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


def obs3_bubble_sort(arr):
    timer_start = time.perf_counter_ns()
    comparison_counter = copy_counter = 0
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
    return comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


def sink_down_sort(arr):
    timer_start = time.perf_counter_ns()
    comparison_counter = copy_counter = 0
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
    return comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


def bi_directional_bubble_sort(arr):
    timer_start = time.perf_counter_ns()
    comparison_counter = copy_counter = 0
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
    return comparison_counter, copy_counter, (timer_end - timer_start) / 1000000


def test_single_algorithm(choice, array):
    if choice == 1:
        data = selection_sort(array)
        print_single_test_results("Selection Sort", len(array), data)
    elif choice == 2:
        data = insertion_sort(array)
        print_single_test_results("Insertion Sort", len(array), data)
    elif choice == 3:
        data = merge_sort(array)
        print_single_test_results("Merge Sort", len(array), data)
    elif choice == 4:
        data = quick_sort(array, 0, len(array) - 1)
        print_single_test_results("Quick Sort", len(array), data)
    elif choice == 5:
        data = heap_sort(array)
        print_single_test_results("Heap Sort", len(array), data)
    elif choice == 6:
        data = bubble_sort(array)
        print_single_test_results("Bubble Sort", len(array), data)
    elif choice == 7:
        data = obs1_bubble_sort(array)
        print_single_test_results("Obs1 Bubble Sort", len(array), data)
    elif choice == 8:
        data=obs2_bubble_sort(array)
        print_single_test_results("Obs2 Bubble Sort", len(array), data)
    elif choice == 9:
        data = obs3_bubble_sort(array)
        print_single_test_results("Obs3 Bubble Sort", len(array), data)
    elif choice == 10:
        data = sink_down_sort(array)
        print_single_test_results("Sink-Down Sort", len(array), data)
    elif choice == 11:
        data = bi_directional_bubble_sort(array)
        print_single_test_results("Bi-Directional Bubble Sort", len(array), data)
    else:
        print("Error: Invalid input")

def test_multiple_algorithms(input_size):
    array = generate_random_integer_set(input_size)
    print("Algorithm Name  |  Array Size  |  No. of Comparisons  |  Run Time (in ms.)")
    for i in range(1, 12):
            test_single_algorithm(i, array)


def print_single_test_results(algorithm, array_size, result_set):
    column_headers = [["Algorithm Name", "Array Size", "No. of Comparisons", "Run Time (in ms.)"]]
    test_data = [[algorithm, array_size, result_set[0], result_set[2]]]
    table_formatter(column_headers, test_data)

def print_table_two():
    input_size = [100, 200, 400, 800, 1000, 2000]
    for i in range(1, 12):
        for j in input_size:
            test_single_algorithm(i, j)
    column_headers = [["Sorting Algorithm", "n=100", "n=200", "n=400", "n=800", "n=1000", "n=2000"]]



def print_table_three():
    column_headers = [["Sorting Algorithm", "n=100", "n=200", "n=400", "n=800", "n=1000", "n=2000"]]



def table_formatter(column_headers, test_data):
    for x in column_headers, test_data:
        print('| {:^20} | {:^20} | {:^20} | {:^20} |'.format(*x))
    for row in test_data:
        print('| {:^20} | {:^20} | {:^20} | {:^20} |'.format(*row))


def main():
    while True:
        print("1. Test an individual sorting algorithm\n2. Test multiple sorting algorithms\n3. Exit")
        user_choice = int(input("Enter choice: "))

        if user_choice == 1:
            print("1. Selection Sort\n2. Insertion Sort\n3. Merge Sort\n4. Quick Sort\n5. Heap Sort\n"
                  "6. Bubble Sort\n7. Obs1 Bubble Sort\n8. Obs2 Bubble Sort\n9. Obs3 Bubble Sort\n"
                  "10. Sink-Down Sort\n11. Bi-Directional Sort")
            print()
            algo_choice = int(input("Enter choice: "))
            array_size = int(input("Enter an array size: "))
            array = generate_random_integer_set(array_size)
            test_single_algorithm(algo_choice, array)
            print()
        if user_choice == 2:
            array_size = int(input("Enter an array size: "))
            # array = generate_random_integer_set(array_size)
            test_multiple_algorithms(array_size)
            print()
        if user_choice == 3:
            print("Goodbye")
            break
main()
