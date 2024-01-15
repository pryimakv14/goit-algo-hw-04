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
    lst = [random.randint(0, 1000) for _ in range(2000)]
    time_insertion = timeit.timeit(lambda: insertion_sort(lst[:]), number=100)
    time_merge = timeit.timeit(lambda: merge_sort(lst[:]), number=100)
    time_timsort = timeit.timeit(lambda: sorted(lst[:]), number=100)

    print(time_insertion, time_merge, time_timsort)
