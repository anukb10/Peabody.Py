# Python Program to implement merge sort using
# multi-threading
import threading
import time
import random

# number of elements in array
MAX = 20

# number of threads
THREAD_MAX = 4

a = [0] * MAX
part = 0

# merge function for merging two parts
def merge(low, mid, high):
    left = a[low:mid+1]
    right = a[mid+1:high+1]

    # n1 is size of left part and n2 is size
    # of right part
    n1 = len(left)
    n2 = len(right)
    i = j = 0
    k = low

    # merge left and right in ascending order
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        a[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = right[j]
        j += 1
        k += 1

# merge sort function
def merge_sort(low, high):
    if low < high:
        # calculating mid point of array
        mid = low + (high - low) // 2

        merge_sort(low, mid)
        merge_sort(mid + 1, high)

        # merging the two halves
        merge(low, mid, high)

# thread function for multi-threading
def merge_sort_threaded():
    global part
    
    # creating 4 threads
    for i in range(THREAD_MAX):
        t = threading.Thread(target=merge_sort, args=(part*(MAX//4), (part+1)*(MAX//4)-1))
        part += 1
        t.start()
        
    # joining all 4 threads
    for i in range(THREAD_MAX):
        t.join()

    # merging the final 4 parts
    merge(0, (MAX // 2 - 1) // 2, MAX // 2 - 1)
    merge(MAX // 2, MAX // 2 + (MAX - 1 - MAX // 2) // 2, MAX - 1)
    merge(0, (MAX - 1) // 2, MAX - 1)

# Driver Code
if __name__ == '__main__':
      # generating random values in array
    for i in range(MAX):
        a[i] = random.randint(0, 100)

     # t1 and t2 for calculating time for
    # merge sort
    t1 = time.perf_counter()

    merge_sort_threaded()

    t2 = time.perf_counter()

    print("Sorted array:", a)
    print(f"Time taken: {t2 - t1:.6f} seconds")