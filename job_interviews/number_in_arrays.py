"""
Даны три неубывающих массива чисел. Найти число, которое присутствует во всех трех массивах.

Input: [1,2,4,5], [3,3,4], [2,3,4,5,6]
Output: 4
"""

import sys

def search(*arrs):
    """
    Ver. 1 of task solving, array merging with bounds

    |   +'1'   |  |+'2' |  |     +'3'  |
    [ 1, 2, 4, 5, 3, 3, 4, 2, 3, 4, 5, 6 ]
    """
    # dividing full array by bounds
    len_arr1 = len(arrs[0])
    len_arr2 = len_arr1 + len(arrs[1])
    len_arr3 = len_arr2 + len(arrs[2])

    arr_full = [*arrs[0], *arrs[1], *arrs[2]]
    arr_search = [0] * (len_arr1 + len_arr2 + len_arr3)
    
    for i in range(len(arr_full)):
        if i < len_arr1:
            arr_search[arr_full[i]] = '1'
        
        elif i >= len_arr1 and i < len_arr2:
            if arr_search[arr_full[i]] == '1':
                arr_search[arr_full[i]] = "{}{}".format(arr_search[arr_full[i]], '2')
            else:
                arr_search[arr_full[i]] = '2'
        
        elif i >= len_arr2 and i < len_arr3:
            if arr_search[arr_full[i]] == '12':
                print("[INFO] Searchable number found -> [%s]" % arr_full[i])
            
        else:
            print("[ERROR] i variable is out of bound, abort..")
            sys.exit(1)
    return

def main():
    print ("\nSearching for number occuring in all of the three arrays")
    a1 = [1,2,4,5]
    a2 = [3,3,4]
    a3 = [2,3,4,5,6]

    search(a1, a2, a3)

if __name__ == '__main__':
    main()