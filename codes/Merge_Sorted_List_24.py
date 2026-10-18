def merge_sorted_lists(list1, list2):
	"""Merge two sorted lists and return a new sorted list."""
	merged = []
	i = j = 0

	while i < len(list1) and j < len(list2):
		if list1[i] <= list2[j]:
			merged.append(list1[i])
			i += 1
		else:
			merged.append(list2[j])
			j += 1

	merged.extend(list1[i:])
	merged.extend(list2[j:])
	return merged

if __name__ == "__main__":
    merge_sorted_lists([1, 3, 5], [2, 4])
    print(merge_sorted_lists([1, 3, 5], [2, 4]))