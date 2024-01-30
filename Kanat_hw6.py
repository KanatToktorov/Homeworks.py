def bubble_sort (numb_list):
    list_length = len(numb_list)
    for i in range (0, list_length-1):
        for j in range (0, list_length-1-i):
            if numb_list [j] > numb_list [j+1]:
                numb_list [j], numb_list [j+1] = numb_list [j+1], numb_list [j]
    return numb_list

unsort_list = [3, 12, -5, 8, 24, 55, 37, 48, 0]
bubble_sort_list = bubble_sort(unsort_list)
print(bubble_sort_list)


def find_num(val, a):
    pos = 0
    resultok = False
    first = 0
    last = len(a) - 1
    while first <= last:
        middle = (first + last) // 2
        if val == a[middle]:
            first = middle
            last = first - 1
            resultok = True
            pos = middle
        elif val > a[middle]:
            first = middle + 1
        else:
            last = middle - 1

    if resultok is True:
        print(f'Элемент найден {val} по индексу {pos}')
    else:
        print(f'Элемент не найден')


a = [1, 4, 12, 15, 18, 22, 25, 31, 36, 40, 42, 48, 52, 55, 56, 60]
find_num(18, a)


