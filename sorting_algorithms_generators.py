def insertion_sort(data):
    for j in range(1, len(data)):
        key = data[j]
        # Insert data[j] into the sorged sequence data[0..j - 1]
        i = j - 1
        while i >= 0 and data[i] > key:
            yield data, i
            data[i + 1] = data[i]
            i -= 1
        data[i + 1] = key
    yield data, -1


def selection_sort(data):
    for i in range(len(data)):
        min = i  # index of minimum
        for j in range(i + 1, len(data)):
            if data[j] < data[min]:
                min = j
            yield data, j
        data[i], data[min] = data[min], data[i]
    yield data, -1



def bubble_sort(data):
    for _ in range(len(data)):
        finished = True
        for j in range(1, len(data)):
            if data[j - 1] > data[j]:
                data[j], data[j - 1] = data[j - 1], data[j]
                finished = False
            yield data, j
        if finished:
            break
    yield data, -1


def merge(data, lo, hi):
    i = lo
    li = 0
    ri = 0
    mi = (lo + hi) // 2

    lhs = data[lo:mi + 1]
    rhs = data[mi + 1:hi + 1]

    while li < len(lhs) and ri < len(rhs):
        yield data, i
        if lhs[li] <= rhs[ri]:
            data[i] = lhs[li]
            li += 1
        else:
            data[i] = rhs[ri]
            ri += 1
        i += 1

    while li < len(lhs):
        yield data, i
        data[i] = lhs[li]
        li += 1
        i += 1

    while ri < len(rhs):
        yield data, i
        data[i] = rhs[ri]
        ri += 1
        i += 1


def _merge_sort(data, lo, hi):
    if lo == hi:
        return
    
    mi = (lo + hi) // 2
    
    yield from _merge_sort(data, lo, mi)
    yield from _merge_sort(data, mi + 1, hi)

    yield from merge(data, lo, hi)


def merge_sort(data):
    yield from _merge_sort(data, 0, len(data) - 1)
    yield data, -1


def heap_sort(data):
    """From ZAL presentations"""
    for start in range((len(data) - 2) // 2, -1, -1):
        yield from move_down(data, start, len(data) - 1)

    for end in range(len(data) - 1, 0, -1):
        data[end], data[0] = data[0], data[end]
        yield from move_down(data, 0, end - 1)
    yield data, -1


def move_down(data, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end: break
        if child + 1 <= end and data[child] < data[child + 1]:
            child += 1
            yield data, child
        if data[root] < data[child]:
            data[root], data[child] = data[child], data[root]
            root = child
            yield data, child
        else:
            break
