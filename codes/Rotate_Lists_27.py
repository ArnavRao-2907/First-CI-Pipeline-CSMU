def rotate_list(items, k):
	"""Return a copy of items rotated k positions to the right."""
	if not items:
		return []

	k %= len(items)
	if k == 0:
		return items.copy()
	return items[-k:] + items[:-k]

if __name__=="__main__":
    print(rotate_list([1, 2, 3, 4, 5], 2))

