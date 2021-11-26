"""Advent of code 2020, day 9: Encoding Error"""

def xmas_cypher(preamble: list[int], number: int) -> bool:
	"""Evaluates validity of input acc. XMAS cypher."""

	for i, num1 in enumerate(preamble):
		for num2 in preamble[1:]:
			if num1 + num2 == number:
				return True

	return False

	
def main(preamble_count: int = 25) -> int:
	"""Returns the first number that does not fit the XMAS cypher."""

	preamble = INPUT_FILE[:preamble_count]
	cyphered_input = INPUT_FILE[preamble_count:]

	for number in cyphered_input:
		if not xmas_cypher(preamble, number):
			return number
		preamble = preamble[1:] + [number]

	return 0

def part_two(preamble_count: int = 25) -> int:
	"""Calculates the encryption weakness in XMAS-encrypted list of numbers.
	"""

	invalid_number = main(preamble_count)
	preceeding = INPUT_FILE[:INPUT_FILE.index(invalid_number)]

	for i, num1 in enumerate(preceeding):
		weak_list = [num1]

		for number in preceeding[i + 1:]:
			if sum(weak_list) < invalid_number:
				weak_list.append(number)
			
		if sum(weak_list) == invalid_number:
			weak_list.sort()
			return weak_list[0] + weak_list[-1]
		
	return 0


if __name__ == "__main__":
	with open("../../input", "r") as file:
		INPUT_FILE = [int(value) for value in file.read().splitlines()]

	print(main(5))
	print(part_two())
