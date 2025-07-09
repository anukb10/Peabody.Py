# Python program to find k largest elements in an 
# array using sorting

def kLargest(arr, k):
    
    # sort the given array in descending order
    arr.sort(reverse=True)
    
    # store the first k elements in result list
    res = arr[:k]
    return res
    
if __name__ == "__main__":
    arr = [1, 23, 12, 9, 30, 2, 50]
    k = 3
    res = kLargest(arr, k)
    print(' '.join(map(str, res)))