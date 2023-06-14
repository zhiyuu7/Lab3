import Lab3 as Lab3

print("Test_Lab3")
# define result as array
# just list down the values for input, dont ref to the source file, eg Lab3.arr
def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    test = [11, 12, 22, 25, 34, 64, 90]

    assert(result == test)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    test = [90, 64, 34, 25, 22, 12, 11]

    assert (result == test)

def test_bubble_sort_over_10():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 66, 34, 19, 10]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    test = 1

    assert(result == test)
def test_bubble_sort_0():
    input_arr = []
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    test = 0

    assert (result == test)

def test_bubble_sort_not_integer():
    input_arr = [64.5, 22.5, 19.9, 77.77, 11, 100]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    test = 2

    assert (result == test)

