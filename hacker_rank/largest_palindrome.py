'''
given a string , what is the size of the largest palindrome substring
eg abaxyxxyxf
largest palindrome : xyxxyx
'''
def findLongestPalindrome(string, leftIndex, rightIndex):

	while leftIndex>=0 and rightIndex<len(string):
		
		if string[leftIndex]!= string[rightIndex]:
			break
	
		leftIndex -= 1
		rightIndex += 1

	##why letindex+1..coz of the while loop above, we have leftindex decremented one too many..
	##hence we increase it by one
	return string[leftIndex + 1:rightIndex]

def longestPalindromicSubstring(string):
    # Write your code here.
	currentLongest = []
	for i in range(1, len(string)):
		
		odd = findLongestPalindrome(string, i-1, i +1)
		even = findLongestPalindrome(string, i-1, i )
		longest = max(odd, even, key = lambda x: len(x))
		currentLongest = max(longest, currentLongest, key = lambda x: len(x))

	return currentLongest	
			
print(longestPalindromicSubstring('abaxyxxyxf'))			
			
			