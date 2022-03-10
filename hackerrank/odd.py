def oddNumbers(l, r):
    return [x for x in range(l, r+1) if x % 2 == 1]

if __name__ == '__main__':
    print(oddNumbers(2, 5))