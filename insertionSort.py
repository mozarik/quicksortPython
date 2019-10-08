# Insertion Sort In Python
#
# Performance Complexity = O(n^2)
# Space Complexity = O(n)

from random import randint
import array

def insertionSort(alist):
    # for every element in our array
    for index in range(1, len(alist)):
        current = alist[index]
        position = index

        while position > 0 and alist[position-1] > current:
            print("Swapped {} for {}".format(alist[position], alist[position-1]))
            alist[position] = alist[position-1]
            print(alist)
            print("===================================================================================================")
            position -= 1
            

        alist[position] = current

    return alist

def randomArray():
    array_list = []
    len_list = input("Banyak nya list : ")
    i = int(len_list)
    
    for x in range (i):
        item_list = randint(1 , 100)
        if item_list in array_list :
            continue
        int_item_list = int(item_list)
        array_list.append(int_item_list)

    alist = array_list
    # print("List yang akan di sorted menggunakan metode quick sort adalah {}".format(alist))
    return alist


alist = randomArray()

print("List yang akan di sorted menggunakan metode INSERTION SORT adalah : {}".format(alist))

insertionSort(alist)

print("Final Sorted List : {}".format(alist))
