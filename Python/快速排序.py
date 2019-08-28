# coding=utf-8
def PARTITION(array, left, right):
    base = array[right]
    i = left - 1
    for j in range(left,right):
        if array[j] <= base:
            i = i + 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

    temp = array[i+1]
    array[i+1] = array[right]
    array[right] = temp
    return i + 1


def QUICKSORT(array, left, right):
    if left >= right:
        return
    q = PARTITION(array, left, right)
    QUICKSORT(array, left, q - 1)
    QUICKSORT(array, q + 1, right)


if __name__ == '__main__':
    l = [9, 10, 11, 7, 1, 2, 3, 6, 5, 8, 4];
    QUICKSORT(l, 0, len(l) - 1)
    print(l)