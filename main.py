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
    return comparison_counter, copy_counter, timer_end - timer_start


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


def test_single_algorithm(choice, array_size):
    array = generate_random_integer_set(array_size)
    if choice == 1:
        data = selection_sort(array)
        print_test_results("Selection Sort", data)
    elif choice == 2:
        insertion_sort(array)
    elif choice == 3:
        merge_sort(array)
    elif choice == 4:
        quick_sort(array, 0, len(array) - 1)
    elif choice == 5:
        heap_sort(array)
    elif choice == 6:
        bubble_sort(array)
    elif choice == 7:
        obs1_bubble_sort(array)
    elif choice == 8:
        obs2_bubble_sort(array)
    elif choice == 9:
        obs3_bubble_sort(array)
    elif choice == 10:
        sink_down_sort(array)
    elif choice == 11:
        bi_directional_bubble_sort(array)
    else:
        print("Error: Invalid input")


def print_test_results(algorithm, result_set):
    print(algorithm)
    print("No. of comparison operations: ", result_set[0])
    print("No. of copy operations: ", result_set[1])
    print("Time taken: ", result_set[2], "(ms)")


def main():
    print("1. Test an individual sorting algorithm")
    print("2. Test multiple sorting algorithms")
    print("3. Exit")
    user_choice = int(input("Enter choice: "))

    test_single_algorithm(user_choice, 20)

    # array = generate_random_integer_set(2000)
    #
    # print()
    # print("Unsorted array:")
    # print(array)
    # print()
    # print()
    #
    # heap_sort(array)
    # #result = bubble_sort(array)
    # print("Sorted array:")
    # print(array)
    # print()
    # #print("Number of comparisons:", results[0])
    # #print("Number of copies:", results[1])
    # #print("Time:", results[2], "(ms)")
    # #print(f"Time: {results[2]:.2f}(ms)")


main()
