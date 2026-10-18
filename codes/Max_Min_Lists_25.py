def find_max_min(numbers):
	if not numbers:
		return None

	maximum = numbers[0]
	minimum = numbers[0]

	for number in numbers[1:]:
		if number > maximum:
			maximum = number
		if number < minimum:
			minimum = number

	return maximum, minimum


if __name__ == "__main__":
	find_max_min([])
	print(find_max_min([]))