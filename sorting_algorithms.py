import random


def test_sorting_algorighm(algoritm, name):
    data = [i for i in range(14)]
    random.shuffle(data)
    
    print(name)
    print(data)
    algoritm(data)
    print(data)


def insertion_sort(data):
    for j in range(1, len(data)):
        key = data[j]
        # Insert data[j] into the sorged sequence data[0..j - 1]
        i = j - 1
        while i >= 0 and data[i] > key:
            data[i + 1] = data[i]
            i -= 1
        data[i + 1] = key


def selection_sort(data):
    for i in range(len(data)):
        min = i  # index of minimum
        for j in range(i + 1, len(data)):
            if data[j] < data[min]:
                min = j
        data[i], data[min] = data[min], data[i]
  

def bubble_sort(data):
    for _ in range(len(data)):
        for j in range(1, len(data)):
            if data[j - 1] > data[j]:
                data[j], data[j - 1] = data[j - 1], data[j]



def merge(data, lo, hi):
    i = lo
    li = 0
    ri = 0
    mi = (lo + hi) // 2

    lhs = data[lo:mi + 1]
    rhs = data[mi + 1:hi + 1]

    while li < len(lhs) and ri < len(rhs):
        if lhs[li] <= rhs[ri]:
            data[i] = lhs[li]
            li += 1
        else:
            data[i] = rhs[ri]
            ri += 1
        i += 1

    while li < len(lhs):
        data[i] = lhs[li]
        li += 1
        i += 1

    while ri < len(rhs):
        data[i] = rhs[ri]
        ri += 1
        i += 1


def _merge_sort(data, lo, hi):
    if lo == hi:
        return
    
    mi = (lo + hi) // 2
    
    _merge_sort(data, lo, mi)
    _merge_sort(data, mi + 1, hi)

    merge(data, lo, hi)


def merge_sort(data):
    _merge_sort(data, 0, len(data) - 1)


def heap_sort(data):
    """From ZAL presentations"""
    for start in range((len(data) - 2) // 2, -1, -1):
        move_down(data, start, len(data) - 1)

    for end in range(len(data) - 1, 0, -1):
        data[end], data[0] = data[0], data[end]
        move_down(data, 0, end - 1)


def move_down(data, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end: break
        if child + 1 <= end and data[child] < data[child + 1]:
            child += 1
        if data[root] < data[child]:
            data[root], data[child] = data[child], data[root]
            root = child
        else:
            break


if __name__ == "__main__":
    test_sorting_algorighm(insertion_sort, "Insertion sort")
    print()
    test_sorting_algorighm(selection_sort, "Selection sort")
    print()
    test_sorting_algorighm(bubble_sort, "Bubble sort")
    print()
    test_sorting_algorighm(merge_sort, "Merge sort")
    print()
    test_sorting_algorighm(heap_sort, "Heap sort")
