def findNumber(arr, k):
    length = arr[0]
    for i in range(length):
        if arr[i] == k:
            return "YES"
    return "NO"

if __name__ == '__main__':
    findNumber([5, 33, 2, 10, 9], 2)