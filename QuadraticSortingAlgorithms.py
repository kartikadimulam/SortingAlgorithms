

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


def insertionSort(list1):
    for index in range(1, len(list1)):

        currentvalue = list1[index]
        position = index

        while position>0 and list1[position-1]>currentvalue:
            list1[position] = list1[position-1]
            position = position-1

        list1[position] = currentvalue

        list1[position-1] = currentvalue
            

            
def mergesort(list1):

    if len(list1) > 1:

        mid = len(list1)//2

        lefthalf = list1[:mid]
        righthalf = list1[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0 #left half index
        j = 0 #right half index
        k =0 #list1 index

        while i<len(lefthalf) and j<len(righthalf):

            if lefthalf[i] <= righthalf[j]:
                list1[k] = lefthalf[i]
                i = i+ 1
            else:
                list1[k] = righthalf[j]
                j= j+ 1

            k = k+1    

            


def test_mergesort():
    numlist1 = [1,2,3,4,5,6,7,8,9]
    numlist2 = [9,8,7,6,5,4,3,2,1]
    numlist3 = []
    numlist4 = [1,9,2,8,3,7,4,5,6]
    numlist5 = [5,4,6,3,7,2,8,1,9]

    mergesort(numlist1)
    mergesort(numlist2)
    mergesort(numlist3)
    mergesort(numlist4)
    mergesort(numlist5)

    assert numlist1 == [1,2,3,4,5,6,7,8,9]
    assert numlist2 == [1,2,3,4,5,6,7,8,9]
    assert numlist3 == []
    assert numlist4 == [1,2,3,4,5,6,7,8,9]
    
    
                
            

    
