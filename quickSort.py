
# Create random array

import random
import array

def randomArray():
    array_list = []
    len_list = input("Banyak nya list : ")
    i = int(len_list)
    
    for x in range (i):
        item_list = input("Masukan item list : ")
        int_item_list = int(item_list)
        array_list.append(int_item_list)

    print(array_list)
        

randomArray()