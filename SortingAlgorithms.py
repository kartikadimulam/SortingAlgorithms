

#Bubble Sort, runs in O(n^2)

def test_bubbleSort():
    list1 = [1,2,4,5,6]
    list2 = [2,2,2,2,2]
    list3 = []
    list4 = [6,7,5,3,1]

    bubbleSort(list1)
    assert list1 == [1,2,4,5,6]

    bubbleSort(list2)
    assert list2 == [2,2,2,2,2]

    bubbleSort(list3)
    assert list3 == []


    bubbleSort(list4)
    assert list4 == [1,3,5,6,7]

# O of n^2

def bubbleSort(list1):

    #must iterate through each sublist of list1
    for passnum in range(len(list1)-1, 0, -1):
        for i in range(passnum):
            if list1[i] > list1[i+1]:
                temp = list1[i]
                list1[i] = list1[i+1]
                list1[i+1] = temp


def test_selectionSort():
    list1 = [1,2,4,5,6]
    list2 = [2,2,2,2,2]
    list3 = []
    list4 = [6,7,5,3,1]

    selectionSort(list1)
    assert list1 == [1,2,4,5,6]

    selectionSort(list2)
    assert list2 == [2,2,2,2,2]

    selectionSort(list3)
    assert list3 == []


    selectionSort(list4)
    assert list4 == [1,3,5,6,7]


# O of n^2

def selectionSort(list1):

    for fillslot in range(len(list1)-1, 0, -1):
        positionofmax = 0
        for location in range(1, fillslot+1):
            if list1[location] > list1[positionofmax]:
                positionofmax = location

            temp = list1[fillslot]
            list1[fillslot] = list1[positionofmax]
            list1[positionofmax] = temp

            

    
                
            

    
