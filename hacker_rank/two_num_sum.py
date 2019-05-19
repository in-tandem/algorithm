'''
func that takes a unsorted array of numbers
and also a target sum
find two numbers which are summed to create target sum
return all such numbers in an array in sorted order

eg
a = [1,-1,3,6,7,5,11]
target = 10
response = [-1,5,6,11]
'''

def twoNumberSum(array, targetSum):
    # Write your code here.
	seq = sorted(array)
	sum = 0
	response = []
	for index, value in enumerate(seq):
	
		for j in seq[index+1:]:
			if value+j == targetSum:
				response.append([value,j])
			elif value + j > targetSum:
				break
    
	return sorted(response)


def threeNumberSum(array, targetSum):
	array.sort()

	response = []

	for index, value in enumerate(array):
		
		newTarget = targetSum - value
		
		twoNumberResponse =  twoNumberSum(array[index+1:], newTarget)
			
		if twoNumberResponse and len(twoNumberResponse)>0:

			for j in twoNumberResponse:
				seq = []
				seq.extend(j)
				seq.append(value)
				seq.sort()
				response.append(seq)
			# twoNumberResponse.append(value)
			# twoNumberResponse.sort()
			

	return response
	

def twoNumberSum1(array, targetSum):
	
	num = {}
	
	for i in array:
		
		potentialMatch = targetSum - i
		
		if potentialMatch in num.keys():
			
			return [i, potentialMatch]
		else:
			num[i] = True
	
	return []


def threeNumberSum1(array, targetSum):

	array.sort()

	triplets = []

	i = 0

	##why len -2 / bcox when we reach the last element in array we cant move any further
	for  i in range( len(array) -2 ):

		left = i + 1
		right = len(array) - 1

		while left < right:
			
			currentSum = array[i] + array[left] + array[right]

			if currentSum == targetSum:
				
				triplets.append([array[i],array[left],array[right]])
				left+= 1
				right -= 1


			elif currentSum < targetSum :

				left+=1

			elif currentSum > targetSum :

				right -= 1

	return triplets






#print(twoNumberSum1([1,-1,3,6,7,5,11],10))
#print(twoNumberSum1([-1,3,2],5))
print(threeNumberSum1([12,3,1,2,-6,5,-8,6], 0))
#print(threeNumberSum([1,2,3,4], 6))