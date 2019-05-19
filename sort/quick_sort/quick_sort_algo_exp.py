## quick sort algorithm as learnt from algoexpert website.

def quicksort(array):
    quickSortHelper(array , 0 , len(array) - 1)
    print(array)

def swap(array, left, right):
    array[left],array[right] = array[right], array[left]

def quickSortHelper(array, leftIndex , rightIndex):

    if leftIndex > rightIndex:
        return

    pivotIndex = leftIndex
    endIndex = rightIndex
    leftIndex += 1

    while leftIndex <= rightIndex:
        
        if array[leftIndex] > array[pivotIndex] and array[rightIndex] < array[pivotIndex]:
            swap(array, leftIndex, rightIndex)

        if array[leftIndex] <= array[pivotIndex]:
            leftIndex += 1

        if array[rightIndex] >= array[pivotIndex]:
            rightIndex -= 1
        

    ##left index has crossed over
    swap(array, pivotIndex, rightIndex)

    leftSubStringShorter = rightIndex - pivotIndex - 1 < endIndex - (rightIndex + 1)

    if leftSubStringShorter:

        quickSortHelper(array, pivotIndex, rightIndex - 1)
        quickSortHelper(array, rightIndex+1, endIndex)

    else:

        quickSortHelper(array, rightIndex+1, endIndex)
        quickSortHelper(array, pivotIndex, rightIndex - 1)

quicksort([22,1,12,3,4,5,0,-1,2,3])