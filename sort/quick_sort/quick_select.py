## quick sort algorithm as learnt from algoexpert website.

def quickselect(array, k):
    response = quickSortHelper(array , 0 , len(array) - 1, k)
    print(response)

def swap(array, left, right):
    array[left],array[right] = array[right], array[left]

def quickSortHelper(array, startIndex , endIndex, nthElement):

    while True:
        
        if startIndex > endIndex:
            return

        pivotIndex = startIndex
        rightIndex = endIndex
        leftIndex  = startIndex + 1

        while leftIndex <= rightIndex:
            
            if array[leftIndex] > array[pivotIndex] and array[rightIndex] < array[pivotIndex]:
                swap(array, leftIndex, rightIndex)

            if array[leftIndex] <= array[pivotIndex]:
                leftIndex += 1

            if array[rightIndex] >= array[pivotIndex]:
                rightIndex -= 1
            

        ##left index has crossed over
        swap(array, pivotIndex, rightIndex)

        if rightIndex == nthElement:
            return array[rightIndex - 1]

        elif rightIndex < nthElement:
            startIndex = rightIndex+1
            
        else:

            endIndex = rightIndex - 1

quickselect([22,1,12,3,4,5,0,-1,2,3],2)