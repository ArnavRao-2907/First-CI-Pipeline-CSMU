def decimal_to_binary(number):
	"""Return the binary representation of an integer as a string."""
	if number == 0:
		return "0"

	sign = "-" if number < 0 else ""
	number = abs(number)
	binary = ""

	while number:
		binary = str(number % 2) + binary
		number //= 2

	return sign + binary

if __name__=="__main__":
    print(decimal_to_binary(3.5))