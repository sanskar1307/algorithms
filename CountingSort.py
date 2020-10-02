'''
Below is the function for counting sort. It is a O(n+k) sorting algorithm, 'n' is the number of elements and 'k' is the range of input.
'''
 
def countingSort(arr): 
	maxEle = max(arr) 
	minEle = min(arr) 
	k = maxEle - minEle + 1
	n = len(arr)
	 
	countArr = [0 for _ in range(k)] 
	outArr   = [0 for _ in range(n)] 

	for i in range(n): 
		countArr[arr[i]-minEle] += 1

	for i in range(1, k): 
		countArr[i] += countArr[i-1] 

	for i in range(n-1, -1, -1): 
		outArr[countArr[arr[i] - minEle] - 1] = arr[i] 
		countArr[arr[i] - minEle] -= 1

	for i in range(n): 
		arr[i] = outArr[i] 

	return arr 
 
arr = [-5, -10, 0, -3, 8, 5, -1, 10] 
ans = countingSort(arr) 
print("Sorted array is " + str(ans)) 

