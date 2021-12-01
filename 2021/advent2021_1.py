"""Advent of Code 2021, day 1: Sonar Sweep"""

def main() -> int:
	"""Count the number of times a depth measurement increases."""

	increased = 0
	depth = int(INPUT_FILE[0])

	for line in INPUT_FILE[1:]:
		measurement = int(line)
		if measurement > depth:
			increased += 1
		depth = measurement

	return increased


def part_two() -> int:
	"""How many sums are larger than the previous sum?"""

	increased = 0
	window_sum = sum([int(i) for i in INPUT_FILE[:3]])

	for i in range(1, len(INPUT_FILE) - 2):
		measurement = sum([int(i) for i in INPUT_FILE[i:i + 3]])
		if measurement > window_sum:
			increased += 1
		window_sum = measurement

	return increased


if __name__ == "__main__":
	with open("../../input", "r") as file:
		INPUT_FILE = file.read().splitlines()

	print(main())
	print(part_two())
