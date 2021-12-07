"""Advent of Code 2021, day 7: The Treachery of Whales

It's the naive approach (ie. search for the optinal solution),
while slow, it still executes within a reasonable timeframe.
"""

import sys

def main(input_stream: tuple[int]) -> int:
	"""
	Determine the horizontal position that the crabs can align to using the least fuel possible.
	How much fuel must they spend to align to that position?
	"""

	# start with a large enough value for spent fuel, we will optimise this
	spent_fuel: int = sys.maxsize

	min_pos = min(input_stream)
	max_pos = max(input_stream)

	for test_pos in range(min_pos, max_pos + 1):
		needed_fuel: int = 0
		for pos in input_stream:
			needed_fuel += abs(test_pos - pos)

		if needed_fuel < spent_fuel:
			spent_fuel = needed_fuel

	return spent_fuel


def part_two(input_stream: tuple[int]) -> int:
	"""
	Determine the horizontal position that the crabs can align to using the least fuel possible.
	How much fuel must they spend to align to that position?

	Similar to main problem, but fuel costs is now the summation of the required movement steps.
	"""

	spent_fuel: int = sys.maxsize

	min_pos = min(input_stream)
	max_pos = max(input_stream)

	for test_pos in range(min_pos, max_pos + 1):
		needed_fuel: int = 0
		for pos in input_stream:
			movement = abs(test_pos - pos)
			needed_fuel += sum(range(movement + 1))

		if needed_fuel < spent_fuel:
			spent_fuel = needed_fuel

	return spent_fuel


if __name__ == "__main__":
	with open("../../input", "r") as file:
		INPUT_FILE = tuple(
			[int(pos) for pos in file.read()[:-1].split(",")]
		)

	print("a: ", main(INPUT_FILE))
	print("b: ", part_two(INPUT_FILE))
