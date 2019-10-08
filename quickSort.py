
# Create random array

from random import randint
import array

def randomArray():
    array_list = []
    len_list = input("Banyak nya list : ")
    i = int(len_list)
    
    for x in range (i):
        item_list = randint(1 , 15)
        if item_list in array_list :
            continue
        int_item_list = int(item_list)
        array_list.append(int_item_list)

    print(array_list)
    return array_list        

randomArray()
    