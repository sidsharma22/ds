def binarySearch(array, target):
	# input: sorted array 
	# 		 target int 
	# output: index of the target int 
	# 		  else: return -1
	# even and odd concept
	# n  and n+1
	# n/2 else n+1/2
	k = len(array)
	end = k-1
	start = 0
	count = 0
	middle = 0
	if target == array[end]:
		return k-1
	elif target == array[0]:
		return 0
	
	if target < array[0] or target > array[end]:
		return -1
	
	# something to start of the loop
	while (count < 2):
			
		if (end - start) %2 == 0:
			calc = int((end - start)/2)
		else:
			calc = int(((end - start)+1)/2)


		middle = start + calc
		if calc == 1:
			count = count + 1

		if target == array[middle]:
			return middle
		elif target > array[middle]:
			start = middle
		else:
			end = middle
	return -1
