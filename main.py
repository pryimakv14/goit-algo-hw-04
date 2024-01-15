import timeit
import random
 

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    def merge(left, right):
        merged = []
        left_index = 0
        right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        while left_index < len(left):
            merged.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            merged.append(right[right_index])
            right_index += 1

        return merged


    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


if __name__ == '__main__':
    lst_small = [random.randint(0, 1000) for _ in range(1000)]
    lst_big = [random.randint(0, 1000) for _ in range(10000)]

    time_insertion_small = timeit.timeit(lambda: insertion_sort(lst_small[:]), number=10)
    time_merge_small = timeit.timeit(lambda: merge_sort(lst_small[:]), number=10)
    time_timsort_small = timeit.timeit(lambda: sorted(lst_small[:]), number=10)

    time_insertion_big = timeit.timeit(lambda: insertion_sort(lst_big[:]), number=10)
    time_merge_big = timeit.timeit(lambda: merge_sort(lst_big[:]), number=10)
    time_timsort_big = timeit.timeit(lambda: sorted(lst_big[:]), number=10)

    print("Сортування вставками - менший список: ", time_insertion_small)
    print("Сортування вставками - більший список: ", time_insertion_big)

    print("Сортування злиттям - менший список: ", time_merge_small)
    print("Сортування злиттям - більший список: ", time_merge_big)

    print("Сортування тімсорт - менший список: ", time_timsort_small)
    print("Сортування тімсорт - більший список: ", time_timsort_big)
