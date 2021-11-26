"""Advent of Code 2020, day 10"""

def tribonacci(num: int = 1) -> int:
	""" "Tribonacci" sequence generator.

	Similar to Fibonacci sequence, but the Nth number is here
	the sum of the last three values.
	"""

	a = 0
	b = 1
	c = 1

	while num:
		yield b
		a, b, c = b, c, a + b + c
		num -= 1


def main() -> int:
	"""
	Returns the number of 1-jolt differences multiplied by
	the number of 3-jolt differences.
	"""

	differences = [0, 0, 0]
	adapted_joltage = 0

	input_main = INPUT_FILE
	input_main.sort()

	for adapter in input_main:
		differences[adapter - adapted_joltage - 1] += 1
		adapted_joltage = adapter

	differences[2] += 1

	return differences[0] * differences[2]


def extra():
	"""
	Computes the total number of distinct ways one can arrange
	the adapters to connect the charging outlet to their device.

	Once the list is sorted, it can be seen that the total number of combinations,
	is the product of all the local combinations. This is defined by how many different ways
	can one arrange a group of 1 differences to still make a valid sequence.

	Having manually checked the first few possible local combinations,
	it became apparent that there was a sequence involved here: "Tribonacci", as shown above!
	"""

	input_extra = INPUT_FILE
	input_extra.sort()
	input_extra = [0] + input_extra + [input_extra[-1] + 3]

	differences = [input_extra[i + 1] - value for i, value in enumerate(input_extra[:-1])]

	# for most cases, creating such a large list will be overkill,
	# this does account for the (unlikely) scenario where there are only 1 differences.
	tribonacci_obj = tuple(tribonacci(differences.count(1)))

	combinations = 1
	counter = 0

	for difference in differences:
		if difference == 1:
			counter += difference
		else:
			combinations *= tribonacci_obj[counter]
			counter = 0

	return combinations


if __name__ == "__main__":
	with open("../../input", "r") as file:
		INPUT_FILE = [int(value) for value in file.read().splitlines()]

	print(main())
	print(extra())
