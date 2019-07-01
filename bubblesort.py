list1 = [64, 34, 25, 12, 22, 11, 90] 
list2 = [1,8,6,54,2,8,9,27,26,15,49,50,39,45,46,47,24,92]

def bubblesort(list):
    for j in range(len(list)-1):
        for i in range(len(list)-1-j):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
    return list


bubblesort(list1)
print(bubblesort(list1))
bubblesort(list2)
print(bubblesort(list2))
