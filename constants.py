# Examples of Constant Time Complexity - O(1)

def sum_of_two_num(x, y):
    return x + y                    # O(1)


def sum_of_three_num(x, y, z):
    return x + y + z                # O(1)


def sum_of_two(x, y):
    a = x                           # O(1)
    b = y                           # O(1)
    return a + b                    # O(1)


def multiply_by_2(a, b, c, d, e):
    a *= 2                          # O(1)
    b *= 2                          # O(1)
    c *= 2                          # O(1)
    d *= 2                          # O(1)
    e *= 2                          # O(1)
    return [a, b, c, d, e]          # O(1)


def sum_of_array():
    arr = [1, 2, 3, 4, 5]           # O(1)
    result = 0                      # O(1)
    for el in arr:                  # O(5)
        result += el                # O(5)
    return result                   # O(1)


def loop_with_return():
    res = 0                         # O(1)
    for i in range(10000000000):    # O(10000000000)
        res += i                    # O(10000000000)
    return res                      # O(1)


def loop_with_no_return():
    for i in range(10000000000):    # O(10000000000)
        if i == 9999999:            # O(9999999)
            print(i)                # O(1)
            break                   # O(1)


def sum_of_four_elms(arr):
    result = 0                      # O(1)
    for i, el in enumerate(arr):    # O(5)
        if i == 4:                  # O(5)
            break                   # O(1)
        result += el                # O(4)
    return result                   # O(1)



def _is_el_exist(arr, i, return_val=False):
    try:
        val = arr[i]                            # O(1)
        if (return_val):                        # O(1)
            return val                          # O(1)
        return True                             # O(1)
    except IndexError:
        return False                            # O(1)

def sum_of_four_elms2(arr):
    result = 0                      # O(1)
    if _is_el_exist(arr, 0):          # O(1)
        result += arr[0]             # O(1)

    if _is_el_exist(arr, 1):          # O(1)
        result += arr[1]             # O(1)

    if _is_el_exist(arr, 2):          # O(1)
        result += arr[2]             # O(1)

    if _is_el_exist(arr, 3):          # O(1)
        result += arr[3]             # O(1)

    return result                   # O(1)

print(sum_of_four_elms2([1,2,5]))

