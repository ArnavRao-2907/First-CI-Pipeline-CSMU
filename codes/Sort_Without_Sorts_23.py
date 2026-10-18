def bubble_sort(numbers):
	"""Sort numbers in ascending order without sort() or sorted()."""
	length = len(numbers)

	for i in range(length):
		swapped = False
		for j in range(length - i - 1):
			if numbers[j] > numbers[j + 1]:
				numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
				swapped = True
		if not swapped:
			break

	return numbers


if __name__ == "__main__":
	print(bubble_sort([1,3,2]))