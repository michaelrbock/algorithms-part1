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
	if len(lst) % 2 == 0:
		middle = (len(lst) / 2) - 1
	else:
		middle = len(lst) / 2

	pivot_choice = get_median( [lst[0], lst[middle], lst[len(lst)-1]] )

	if pivot_choice == lst[0]:
		PIVOT_INDEX = 0
	elif pivot_choice == lst[middle]:
		PIVOT_INDEX = middle
	elif pivot_choice == lst[len(lst)-1]:
		PIVOT_INDEX = len(lst) - 1

	pivot = lst[PIVOT_INDEX]
	lst[0], lst[PIVOT_INDEX] = lst[PIVOT_INDEX], lst[0]
	i = 1
	for j in range(1, len(lst)):
		if lst[j] < pivot:
			lst[j], lst[i] = lst[i], lst[j]
			i += 1
	lst[0], lst[i-1] = lst[i-1], lst[0]
	return lst, i

def get_median(nums):
	values = sorted(nums)
	if len(values) % 2 == 1:
		return values[(len(values)+1)/2-1]
	else:
		lower = values[len(values)/2-1]
		upper = values[len(values)/2]
	return (lower+upper)/2

def quicksort_wrapper(lst):
	result = quicksort(lst)
	print result, comparisons
