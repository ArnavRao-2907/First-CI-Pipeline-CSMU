import string

def is_anagram(first, second):
	first = first.lower()
	second = second.lower()

	if len(first) != len(second):
		return False

	character_counts = {}
	for character in first:
		character_counts[character] = character_counts.get(character, 0) + 1

	for character in second:
		if character not in character_counts:
			return False
		character_counts[character] -= 1
		if character_counts[character] < 0:
			return False

	return True

if __name__ == "__main__":
	is_anagram("", "Silent")
