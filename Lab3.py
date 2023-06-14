print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):

    # Copy input list to results list
    arr_result = arr.copy()

    # Get number of elements in the list
    n = len(arr_result)

    if n==0:
        print("Empty array")
        return 0

    for value in arr_result:
        if not isinstance(value, int):
            print("Array contains non-integer element(s)")
            return 2

    if n < 10:
        # Traverse through all array elements
        for i in range(n - 1):
            # range(n) also work but outer loop will
            # repeat one time more than needed.

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                if sorting_order == SORT_ASCENDING:
                    if arr_result[j] > arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]


                elif sorting_order == SORT_DESCENDING:
                    if arr_result[j] < arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]


                else:
                    # Return an empty array
                    arr_result = []

        return arr_result


    elif n >= 10: # REQ-03
        print("Array has " + str(n)+ " elements, max allowed is 9!")
        return 1


def main():
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90]

    # Sort in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order: ")
    print("Return: " + str(result))

    # Sort in descending order
    print("Sorted array in ascending order: ")
    result = bubble_sort(arr, SORT_DESCENDING)
    print("Return: " + str(result))

    arr_long = [64, 34, 25, 12, 22, 11, 90, 66, 34, 19, 10] # 11 elements
    print("Try to sort an empty array with equal or more than 10 elements")
    result = bubble_sort(arr_long, SORT_ASCENDING)
    print("Return: " + str(result))

    arr_empty = []
    print("Try to sort an empty array")
    result = bubble_sort(arr_empty, SORT_ASCENDING)
    print("Return: " + str(result))

    arr_not_integer = [64.5, 22.5, 19.9, 77.77, 11, 100]
    print("Try to sort a non-integer array")
    result = bubble_sort(arr_not_integer, SORT_ASCENDING)
    print("Return: " + str(result))

if __name__ == "__main__":
    main()


