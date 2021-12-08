"""Advent of Code 2021, day 8: Seven Segment Search

Method used for part one will not work for part two.
"""

def main(input_stream: list[str]) -> int:
	"""In the output values, how many times do digits 1, 4, 7, or 8 appear?"""

	counter: int = 0

	for stream in input_stream:
		signal_pattern, _, output_pattern = stream.partition("|")
		output_pattern = output_pattern.split()

		for pattern in output_pattern:
			if (
				len(pattern) == 2 or\
				len(pattern) == 4 or\
				len(pattern) == 3 or\
				len(pattern) == 7
			):
				counter += 1

	return counter


def part_two():
	"""
	"""
	raise NotImplementedError


if __name__ == "__main__":
	with open("../../input", "r") as file:
		INPUT_FILE = tuple(file.read().splitlines())


	print("1: ", main(INPUT_FILE))
#	print("2: ", part_two())
