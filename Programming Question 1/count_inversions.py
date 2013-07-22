def count_splits(left, right):
    print "L ", left
    print "R ", right
    result = []
    inversions = 0
    # continue assigning elements to result until left and right
    # are empty
    while len(left) > 0 or len(right) > 0:
    	# if there are elements in both lists
        if len(left) > 0 and len(right) > 0:
			# compare the first elements of each list
            if left[0] <= right[0]:
				# append the smaller element to the result list
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
                inversions += len(left)
		# if one array is empty, append the other one in its
        # entirety to result
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))
	# end while
    print "I ", inversions
    return result, inversions

def count(lst):
	# if list size is empty or 1, it is sorted and return it
    if len(lst) <= 1:
        return lst, 0

	# else, list size is > 1, so split into 2 sublists
	# 1. Divide
    middle = len(lst) / 2 # integer
    left = lst[:middle]
    right = lst[middle:]
	
	# recursively call merge_sort on each list
    l_result = count(left)
    left = l_result[0]
    l_count = l_result[1]
    r_result = count(right)
    right = r_result[0]
    r_count = r_result[1]

	# 2. Conquer
    res = count_splits(left, right)
    return res[0], res[1] + l_count + r_count

a = [6,5,4,3,2,1]
print count(a)
