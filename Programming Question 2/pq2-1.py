comparisons = 0 # global

def quicksort(lst):
	global comparisons
	if len(lst) <= 1:
		return lst
	lst, store_index = partition(lst)
	comparisons += len(lst[:store_index-1])
	comparisons += len(lst[store_index:])
	return quicksort(lst[:store_index-1]) + [lst[store_index-1]] + quicksort(lst[store_index:])

def partition(lst):
	PIVOT_INDEX = 0
	pivot = lst[PIVOT_INDEX]
	i = 1
	for j in range(1, len(lst)):
		if lst[j] < pivot:
			lst[j], lst[i] = lst[i], lst[j]
			i += 1
	lst[0], lst[i-1] = lst[i-1], lst[0]
	return lst, i

def quicksort_wrapper(lst):
	result = quicksort(lst)
	print result, comparisons
