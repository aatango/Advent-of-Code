def advent_1 (input: list, target_sum: int) -> int:
	""" Product of numbers that sum to X

	Day 1 of Advent of Code 2020: achieve target_sum with only two numbers.
	"""

	for i, v in enumerate(input):
		for u in input[i:]:
			if v + u == target_sum: return u * v


def advent_1b (input: list) -> int:
	""" Product of numbers that sum to X

	Part two of Day 1: achieve target_sum with three numbers.
	"""

	target_sum = 2020
	
	for i, v in enumerate(input):
		for j, u in enumerate(input[i:]):
			for w in input[j:]:
				if v + u + w == target_sum: return u * v * w


if __name__ == "__main__":
	example_input = [1721, 979, 366, 299, 675, 1456]

	with open("../input.txt", 'r') as file:
		input = [int(number) for number in file.read().split()]

	print("Day 1: ", advent_1(input, 2020))
	print("Part two: ", advent_1b(input, 2020))
