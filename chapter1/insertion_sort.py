"""
Best Case - O(n)
Average Case - O(n²)
Worst Case - O(n²)
"""

array1 = [5, 2, 4, 6, 1, 3]

array2 = [31, 41, 59, 26, 41, 58]

def insertion_sort_increasing(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        print("I {} KEY {} J {} A[j] {}".format(i, key, j, array[j]))

        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
            print("cond", array)

        array[j+1] = key

        print(array)

    return array

def insertion_sort_decreasing(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        print("I {} KEY {} J {} A[j] {}".format(i, key, j, array[j]))

        while j >= 0 and array[j] < key:
            array[j+1] = array[j]
            j -= 1
            print("cond", array)

        array[j+1] = key

        print(array)

    return array

insertion_sort_decreasing(array1)