
# Create random array

from random import randint
import array

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

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   
   print("Step by Step of A List Changing Very Iteration Iteration :    {}".format(alist))


   return rightmark

alist = randomArray()

print("List yang akan di sorted menggunakan metode quick sort adalah : {}".format(alist))

quickSort(alist)

print("Final Sorted List : \t\t\t\t\t      {}".format(alist))
    