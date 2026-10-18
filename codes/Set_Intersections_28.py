def set_intersection(first, second):
	"""Return the distinct elements shared by first and second."""
	intersection = []

	for first_item in first:
		found_in_second = False
		for second_item in second:
			if first_item == second_item:
				found_in_second = True
				break

		if found_in_second:
			already_added = False
			for result_item in intersection:
				if first_item == result_item:
					already_added = True
					break

			if not already_added:
				intersection.append(first_item)

	return intersection

if __name__=="__main__":
    print(set_intersection({1, 2, 3}, {2, 3, 4}))
